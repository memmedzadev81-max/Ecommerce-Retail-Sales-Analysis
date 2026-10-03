# 🛒 Ecommerce Retail Sales Analysis

> Statistical analysis of e-commerce transactions — **RFM segmentation**, hypothesis testing, cohort retention and actionable retail insights.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458) ![SciPy](https://img.shields.io/badge/SciPy-Statistics-8caae6) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 1. Project Overview

This project turns raw e-commerce order data into a clear customer-value and retention picture.

**Workflow:** Data Cleaning → EDA → RFM Segmentation → Statistical Testing → Cohort Retention → Business Recommendations.

---

## 🎯 2. Business Objectives

1. Identify high-value customers with **RFM** (Recency, Frequency, Monetary).
2. Test whether key segments differ statistically (spending, frequency, retention).
3. Measure cohort retention over time.
4. Turn findings into prioritised marketing and retention actions.

---

## 📂 3. Dataset

| Item | Detail |
|------|--------|
| Type | E-commerce order / transaction level |
| Focus | Customer ID, Order Date, Order Value, Product Category |
| Analysis methods | RFM scoring, Chi-square / T-tests, Cohort tables |

> Place your cleaned CSV in `data/ecommerce_orders.csv` (or update the path in `analysis.py`).

**Expected columns (example):** `customer_id`, `order_id`, `order_date`, `order_value`, `product_category`, `quantity`.

---

## 🛠️ 4. Technologies Used

- **Python 3**
- **Pandas / NumPy** — cleaning & aggregation
- **Matplotlib / Seaborn** — visualisation
- **SciPy** — statistical tests
- **Jupyter** — exploratory work

---

## 🧹 5. Data Cleaning (planned steps)

1. Parse dates and handle missing / invalid order values.
2. Remove cancelled / zero-value orders if present.
3. Create analysis-ready features: order month, customer first order date, monetary totals.

---

## 📈 6. Analysis Modules

### RFM Segmentation
- **Recency** — days since last purchase
- **Frequency** — number of orders
- **Monetary** — total spend
- Score 1–5 per dimension → segment labels (Champions, Loyal, At Risk, Hibernating, etc.)

### Statistical Tests
- Compare average order value / frequency across RFM segments
- Test association between category preference and high-value status

### Cohort Retention
- Monthly cohorts by first purchase month
- Retention % in subsequent months

---

## 💡 7. Key Business Questions Answered

| # | Question |
|---|----------|
| 1 | Who are the Champions and how much do they contribute? |
| 2 | Which customers are At Risk and worth winning back? |
| 3 | Do high-frequency customers also have higher AOV? |
| 4 | How does retention decay by cohort? |
| 5 | Which product categories drive the top RFM segments? |

---

## 🧭 8. Business Recommendations (template)

1. **Protect Champions** — exclusive offers, early access, VIP support.
2. **Win-back At Risk** — time-limited discounts + personalised product suggestions.
3. **Grow Loyal → Champions** — frequency incentives and cross-sell bundles.
4. **Use cohort insights** — improve onboarding in the first 30–60 days where retention drops most.

---

## 📁 9. Project Structure

```
Ecommerce-Retail-Sales-Analysis/
├── data/                    # place ecommerce_orders.csv here
├── notebooks/
│   └── ecommerce_analysis.ipynb
├── images/                  # charts (RFM, cohort, AOV etc.)
├── analysis.py              # runnable analysis script
├── requirements.txt
└── README.md
```

---

## ▶️ 10. How to Run

```bash
git clone https://github.com/memmedzadev81-max/Ecommerce-Retail-Sales-Analysis.git
cd Ecommerce-Retail-Sales-Analysis
pip install -r requirements.txt

# Add your data to data/ecommerce_orders.csv then:
python analysis.py
# or open notebooks/ecommerce_analysis.ipynb
```

---

## 👤 11. Author

**Vusal Mammadzade** — Data Analyst  
GitHub: [memmedzadev81-max](https://github.com/memmedzadev81-max)

*Part of my data analytics portfolio. Feedback welcome!*
