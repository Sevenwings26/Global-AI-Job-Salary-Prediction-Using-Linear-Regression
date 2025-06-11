# 💼 Global AI Job Salary Prediction Using Linear Regression

Data Source: `kaggle.com`

> Predicting annual salary in USD based on job features like title, experience level, and location.

---

## 📌 Project Overview

This project aims to build a **Linear Regression** model that predicts job salaries in USD using various job-related features such as:

- Job title  
- Experience level  
- Years of experience  
- Employment type  
- Remote ratio  
- Education level  
- Industry  
- Company size  

The goal is to help candidates, HR professionals, and job boards estimate salary ranges for tech-related roles using historical job posting data.

---

## 🧠 Problem Statement

> How can we accurately predict a job's salary in USD given its title, required experience, and other posting features?

---

## 📂 Dataset Description
 - Chech the data dictionary file for Details.

The dataset consists of job postings with the following columns:

| Feature               | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| `job_title`            | Job title (e.g., Data Scientist, ML Engineer)                    |
| `salary_usd`           | Target: Annual salary in USD                                     |
| `experience_level`     | EN (Entry), MI (Mid), SE (Senior), EX (Executive)                |
| `employment_type`      | FT (Full-time), PT, CT, FL                                       |
| `company_location`     | Country where the company is located                             |
| `employee_residence`   | Country of employee residence                                     |
| `remote_ratio`         | 0 = Onsite, 50 = Hybrid, 100 = Fully Remote                       |
| `company_size`         | S (<50), M (50–250), L (>250)                                     |
| `education_required`   | Minimum required education level                                 |
| `years_experience`     | Required years of experience                                     |
| `job_category`         | Domain (e.g., AI Researcher, Data Analyst)                       |
| `industry`             | Company industry                                                 |
| `required_skills`      | Top 5 required skills (comma-separated)                          |
| `benefits_score`       | Numerical rating of benefits (1–10)                              |
| `job_description_length` | Length of job description (character count)                    |

---

## 📊 Exploratory Data Analysis (EDA)

Key EDA steps included:

- Distribution of salaries across job titles and experience levels
- Correlation between numeric features (e.g., experience vs salary)
- Boxplots of salary by employment type and company size
- Handling missing values and encoding categorical variables

---

## 🔧 Machine Learning Approach

| Step                      | Details                                                        |
|---------------------------|----------------------------------------------------------------|
| Model Type                | Linear Regression                                              |
| Preprocessing             | One-hot/Ordinal encoding, scaling                             |
| Feature Selection         | Removed multicollinearity, encoded job-level variables        |
| Train-Test Split          | 80% train / 20% test                                           |
| Evaluation Metrics        | R² Score, MAE, RMSE                                            |

---

## ✅ Model Results

| Metric        | Score      |
|---------------|------------|
| MAE           | 41,000 |

---

## 🧾 Key Insights

- Seniority level and job title are strong predictors of salary.
- Remote-friendly jobs tend to have higher average salaries.
- Education level and company size also show strong correlations.
- Job descriptions with more detail are often linked to higher pay.

---

## 🚀 Future Improvements

- Try Ridge/Lasso Regression for regularization  
- Explore Tree-based models (Random Forest, XGBoost)  
- Build a Streamlit app to allow real-time predictions  
- Improve feature engineering for skills and industries  

---

## 🛠️ Tech Stack

- Python 3.10
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Jupyter Notebook

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Sevenwings26/Global-AI-Job-Salary-Prediction-Using-Linear-Regression.git
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the notebook:

   ```bash
   jupyter notebook notebooks/salary_prediction.ipynb
   ```

---

## 📫 Contact

For questions, collaborations, or feedback:

**Iyanu Arowosola**
📧 iarowosola@yahoo.com
🔗 [LinkedIn Profile](https://linkedin.com/in/iyanuarowosola)

---

*This project was developed as part of a machine learning portfolio targeting job market insights in the tech and data space.*
