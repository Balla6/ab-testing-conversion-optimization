# A/B Testing Conversion Optimization

## Executive Summary

This project evaluates whether a new product experience improves user conversion rates using an A/B testing framework.

The treatment group achieved a **15.53%** conversion rate compared to **10.53%** for the control group, representing an **absolute uplift of 5.01 percentage points** and a **relative improvement of 47.6%**.

A two-proportion Z-test confirms that the difference is **statistically significant**, and power analysis indicates that the experiment had sufficient sample size to detect the observed effect.

The treatment also outperformed the control group across all geographic segments (**US, UK, Canada**), suggesting that the improvement is stable rather than isolated to a single region.

Based on the observed uplift, deploying the treatment to a population of roughly **70,000 users** could generate approximately **3,500 additional conversions**.

**Recommendation:** Roll out the treatment experience globally.

---

# Project Overview

A product team introduced a new webpage experience intended to improve user conversions. The goal of this analysis is to determine whether the treatment version leads to a statistically significant improvement in conversion performance compared to the control version.

Using A/B testing methodology, the project evaluates the experiment results, quantifies the treatment effect, and estimates the potential business impact of deploying the new experience.

---

# Why This Project Matters

A/B testing is one of the most important tools in product analytics and experimentation. Product teams must determine not only whether a metric changed, but whether the change is **statistically reliable, practically meaningful, and consistent across user segments**.

This project demonstrates a realistic experimentation workflow including:

- validating experiment data
- estimating conversion uplift
- testing statistical significance
- quantifying uncertainty using confidence intervals
- evaluating sample adequacy through power analysis
- assessing performance across geographic segments
- translating experiment results into business impact

---

# Dataset

The dataset contains user-level experiment observations with the following fields:

- **country** — geographic segment of the user  
- **group** — experiment assignment (control or treatment)  
- **converted** — whether the user completed the conversion event (0 or 1)

**Total observations:**  
**69,889 users**

Country distribution:

- United States ≈ 70%
- United Kingdom ≈ 25%
- Canada ≈ 5%

---

# Methodology

The experiment analysis follows a structured experimentation workflow.

### 1. Data validation and quality checks

- dataset structure verification  
- missing value checks  
- experiment group balance validation  

### 2. Conversion rate analysis

- conversion rate for control vs treatment  
- absolute and relative uplift estimation  

### 3. Statistical hypothesis testing

- two-proportion Z-test  
- significance evaluation  

### 4. Confidence interval estimation

- 95% confidence intervals for conversion rates  
- uncertainty assessment  

### 5. Power analysis

- evaluation of sample size adequacy  
- confirmation that the experiment had sufficient statistical power  

### 6. Segment-level analysis

- conversion performance by country  
- evaluation of treatment consistency across geographic segments  

### 7. Business impact estimation

- projected additional conversions if the treatment is deployed  

### 8. Product recommendation

- experiment-based rollout decision  

---

# Key Results

| Metric | Control | Treatment |
|------|------|------|
| Conversion Rate | **10.53%** | **15.53%** |

**Absolute uplift:**  
+ **5.01 percentage points**

**Relative uplift:**  
+ **47.6% improvement**

The difference between the groups is **highly statistically significant**, indicating that the observed improvement is unlikely to be due to random variation.

---

# Business Impact

If the treatment experience were deployed to approximately **70,000 users**, the expected impact would be:

**≈ 3,500 additional conversions**

The treatment effect is consistent across geographic segments, suggesting the improvement is not limited to a single region.

---

# Visualizations

### Conversion Rate Comparison

![Conversion Comparison](visualizations/conversion_rate_comparison.png)

### Conversion Rate by Country

![Country Conversion](visualizations/country_conversion_comparison.png)

### Conversion Rate with 95% Confidence Intervals

![Confidence Intervals](visualizations/conversion_confidence_intervals.png)

---

# Recommendation

Based on the statistical evidence and observed business impact, the treatment version demonstrates a substantial improvement in conversion performance.

The experiment results support **rolling out the treatment experience globally**, as it produces a meaningful and statistically significant increase in conversions.

---

# Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Statsmodels  
- Jupyter Notebook  

---

# Project Structure

```
ab-testing-conversion-experiment
│
├── config
│   └── config.yaml
│
├── data
│   └── ab_data.csv
│
├── notebooks
│   └── experiment_analysis.ipynb
│
├── src
│   ├── experiment_utils.py
│   └── stats_tests.py
│
├── visualizations
│   ├── conversion_rate_comparison.png
│   ├── country_conversion_comparison.png
│   └── conversion_confidence_intervals.png
│
├── README.md
└── requirements.txt
```

---

# Reproducibility

To run this project locally:

1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Open `notebooks/experiment_analysis.ipynb`
4. Run the notebook from top to bottom

Example setup:

```bash
git clone https://github.com/Balla6/ab-testing-conversion-optimization.git
cd ab-testing-conversion-optimization
pip install -r requirements.txt
```
Reusable statistical functions are implemented in:
- src/stats_tests.py
- src/experiment_utils.py

# Skills Demonstrated

- A/B experimentation design
- Statistical hypothesis testing
- Confidence interval estimation
- Statistical power analysis
- Segment-level analytics
- Business impact evaluation
- Data visualization
- Analytical storytelling
