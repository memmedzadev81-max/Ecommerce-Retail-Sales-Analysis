# Ecommerce Retail Sales Analysis

RFM segmentation on **order-level** data: who buys often, who spends, who went quiet.

Sample data is created automatically when you run the script (or put your own CSV in `data/ecommerce_orders.csv`).

This is **not** a claim of “1M+ real transactions”. It is a reproducible RFM workflow you can point at a real export.

---

## vs my other projects

| Repo | Focus |
|------|--------|
| `supermarket-sales-analysis` | Store branches + significance tests |
| `customer-shopping-sales-analysis` | Mall categories / demographics |
| `customer-personality-analysis` | RFM + K-Means + campaign response |
| **This repo** | Order RFM segments + simple stats |

---

## Questions

1. How are customers split by Recency, Frequency, Monetary?
2. How much revenue sits in Champions vs Hibernating?
3. Do Champions spend differently from the rest (t-test)?
4. Which product categories lead in the sample?

---

## Data

Expected columns:

- `customer_id`, `order_id`, `order_date`, `order_value`
- optional: `product_category`, `quantity`

Path: `data/ecommerce_orders.csv`  
If the file is missing, `analysis.py` builds a small sample so the pipeline still runs.

---

## Stack

Python · pandas · numpy · matplotlib · seaborn · scipy

---

## How to run

```bash
pip install -r requirements.txt
python analysis.py
```

Charts → `images/`

---

## Structure

```
Ecommerce-Retail-Sales-Analysis/
├── data/                 # optional CSV; sample auto-created
├── images/
├── analysis.py
├── requirements.txt
└── README.md
```

---

Vusal Mammadzade · [memmedzadev81-max](https://github.com/memmedzadev81-max)
