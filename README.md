# Ecommerce Retail Sales Analysis

**Status:** analysis **code and README are ready**; put an order-level CSV in `data/` to run full RFM and charts.

This project is about **customer value over time** (RFM + cohorts), not branch KPIs and not mall category mix.

---

## How it differs from my other sales work

| Repo | Focus |
|------|--------|
| `supermarket-sales-analysis` | 3 stores, ops + significance tests |
| `customer-shopping-sales-analysis` | Malls and product categories |
| `sql-sales-analysis` | Retail KPIs in SQL only |
| **This repo** | RFM segments, retention cohorts |

---

## Goals

1. Score customers with Recency, Frequency, Monetary
2. Compare segments with simple stats where useful
3. Build monthly cohorts by first purchase
4. Suggest who to protect, win back, or grow

---

## Data you need

Place a file at `data/ecommerce_orders.csv` with at least:

- `customer_id`
- `order_id`
- `order_date`
- `order_value`

Optional: `product_category`, `quantity`.

---

## Stack

Python · pandas · numpy · matplotlib · seaborn · scipy

---

## Structure

```
Ecommerce-Retail-Sales-Analysis/
├── data/           # add ecommerce_orders.csv here
├── notebooks/
├── images/
├── analysis.py     # RFM + distribution charts
├── requirements.txt
└── README.md
```

```bash
pip install -r requirements.txt
python analysis.py
```

Without the CSV, the script exits cleanly and tells you what is missing.

---

Vusal Mammadzade · [memmedzadev81-max](https://github.com/memmedzadev81-max)
