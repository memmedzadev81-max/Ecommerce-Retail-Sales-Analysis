"""
Ecommerce Retail Sales Analysis — RFM + segment summary.
Creates sample orders CSV if data/ecommerce_orders.csv is missing.
"""
from pathlib import Path
import random
from datetime import datetime, timedelta

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "ecommerce_orders.csv"
IMG_DIR = BASE / "images"
IMG_DIR.mkdir(exist_ok=True)
(BASE / "data").mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")
random.seed(42)


def ensure_sample(path: Path) -> None:
    if path.exists():
        return
    customers = list(range(1, 151))
    start = datetime(2023, 1, 1)
    cats = ["Electronics", "Home", "Fashion", "Beauty", "Sports", "Books"]
    rows = []
    oid = 1000
    for c in customers:
        n = random.choice([1, 1, 2, 2, 3, 4])
        for _ in range(n):
            oid += 1
            day = start + timedelta(days=random.randint(0, 500))
            rows.append(
                {
                    "customer_id": c,
                    "order_id": oid,
                    "order_date": day.strftime("%Y-%m-%d"),
                    "order_value": round(random.uniform(20, 220), 2),
                    "product_category": random.choice(cats),
                    "quantity": random.randint(1, 4),
                }
            )
    for c in range(1, 20):
        for _ in range(random.randint(5, 9)):
            oid += 1
            day = start + timedelta(days=random.randint(350, 500))
            rows.append(
                {
                    "customer_id": c,
                    "order_id": oid,
                    "order_date": day.strftime("%Y-%m-%d"),
                    "order_value": round(random.uniform(90, 350), 2),
                    "product_category": random.choice(cats),
                    "quantity": random.randint(1, 3),
                }
            )
    pd.DataFrame(rows).to_csv(path, index=False)
    print(f"Created sample data: {path} ({len(rows)} rows)")


def load_data(path: Path) -> pd.DataFrame:
    ensure_sample(path)
    df = pd.read_csv(path, parse_dates=["order_date"])
    print(f"Loaded {len(df):,} rows, {df['customer_id'].nunique()} customers")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["customer_id", "order_date", "order_value"])
    return df[df["order_value"] > 0].copy()


def rfm_table(df: pd.DataFrame) -> pd.DataFrame:
    analysis_date = df["order_date"].max() + pd.Timedelta(days=1)
    rfm = (
        df.groupby("customer_id")
        .agg(
            recency=("order_date", lambda x: (analysis_date - x.max()).days),
            frequency=("order_id", "nunique"),
            monetary=("order_value", "sum"),
        )
        .reset_index()
    )
    rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["M"] = pd.qcut(rfm["monetary"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)

    def label(row):
        if row["R"] >= 4 and row["F"] >= 4 and row["M"] >= 4:
            return "Champions"
        if row["R"] >= 3 and row["F"] >= 3:
            return "Loyal"
        if row["R"] >= 4 and row["F"] <= 2:
            return "New / Promising"
        if row["R"] <= 2 and row["F"] >= 3:
            return "At Risk"
        if row["R"] <= 2 and row["F"] <= 2:
            return "Hibernating"
        return "Others"

    rfm["segment"] = rfm.apply(label, axis=1)
    return rfm


def segment_summary(rfm: pd.DataFrame):
    s = (
        rfm.groupby("segment")
        .agg(
            customers=("customer_id", "count"),
            revenue=("monetary", "sum"),
            avg_orders=("frequency", "mean"),
        )
        .sort_values("revenue", ascending=False)
    )
    s["revenue_share_pct"] = (s["revenue"] / s["revenue"].sum() * 100).round(1)
    s["customer_share_pct"] = (s["customers"] / s["customers"].sum() * 100).round(1)
    print("\n=== Segments ===")
    print(s.to_string())
    return s


def charts(rfm, df):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, col, title in zip(
        axes, ["recency", "frequency", "monetary"], ["Recency", "Frequency", "Monetary"]
    ):
        sns.histplot(rfm[col], ax=ax, kde=True, color="#2c7fb8")
        ax.set_title(title)
    plt.tight_layout()
    fig.savefig(IMG_DIR / "01_rfm_distributions.png", dpi=120)
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 4))
    order = rfm["segment"].value_counts().index
    sns.countplot(data=rfm, y="segment", order=order, ax=ax, color="#2c7fb8")
    ax.set_title("Customers by segment")
    plt.tight_layout()
    fig.savefig(IMG_DIR / "02_segments.png", dpi=120)
    plt.close()

    if "product_category" in df.columns:
        fig, ax = plt.subplots(figsize=(8, 4))
        df.groupby("product_category")["order_value"].sum().sort_values().plot(
            kind="barh", ax=ax, color="#2c7fb8"
        )
        ax.set_title("Revenue by category")
        plt.tight_layout()
        fig.savefig(IMG_DIR / "03_category_revenue.png", dpi=120)
        plt.close()
    print("Charts saved to images/")


def main():
    print("=== Ecommerce Retail Sales Analysis ===")
    df = clean(load_data(DATA_PATH))
    rfm = rfm_table(df)
    segment_summary(rfm)
    champ = rfm.loc[rfm["segment"] == "Champions", "monetary"]
    other = rfm.loc[rfm["segment"] != "Champions", "monetary"]
    if len(champ) > 2 and len(other) > 2:
        t, p = stats.ttest_ind(champ, other, equal_var=False)
        print(f"\nT-test monetary Champions vs rest: t={t:.2f}, p={p:.4g}")
    charts(rfm, df)
    print("Done.")


if __name__ == "__main__":
    main()
