"""
Ecommerce Retail Sales Analysis
RFM segmentation, basic stats and cohort skeleton.
Place data/ecommerce_orders.csv before running.
"""

import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Paths
BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "ecommerce_orders.csv"
IMG_DIR = BASE / "images"
IMG_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"[!] Data file not found: {path}")
        print("    Add your ecommerce orders CSV and re-run.")
        print("    Expected columns example: customer_id, order_id, order_date, order_value")
        return pd.DataFrame()
    df = pd.read_csv(path, parse_dates=["order_date"], dayfirst=False)
    print(f"Loaded {len(df):,} rows from {path.name}")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.dropna(subset=["customer_id", "order_date", "order_value"])
    df = df[df["order_value"] > 0].copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df


def rfm_table(df: pd.DataFrame, analysis_date=None) -> pd.DataFrame:
    if df.empty:
        return df
    if analysis_date is None:
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
    # Quintile scores (1–5)
    rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["M"] = pd.qcut(rfm["monetary"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["RFM_Score"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)
    return rfm


def plot_rfm_distribution(rfm: pd.DataFrame):
    if rfm.empty:
        return
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    for ax, col, title in zip(axes, ["recency", "frequency", "monetary"], ["Recency (days)", "Frequency", "Monetary"]):
        sns.histplot(rfm[col], ax=ax, kde=True)
        ax.set_title(title)
    plt.tight_layout()
    out = IMG_DIR / "01_rfm_distributions.png"
    plt.savefig(out, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"Saved {out.name}")


def main():
    print("=== Ecommerce Retail Sales Analysis ===")
    df = load_data(DATA_PATH)
    df = clean(df)
    if df.empty:
        print("\nSkeleton ready. Add data and re-run to generate RFM and charts.")
        return
    rfm = rfm_table(df)
    print("\nRFM sample:")
    print(rfm.head(10).to_string(index=False))
    print(f"\nCustomers scored: {len(rfm):,}")
    plot_rfm_distribution(rfm)
    print("\nDone.")


if __name__ == "__main__":
    main()
