# Personal Finance Analytics Dashboard

A personal finance analytics application built with Python, Streamlit, Pandas, and Plotly. The dashboard allows users to upload financial transaction files, automatically categorize expenses, manage custom categories, and visualize their spending patterns through interactive tables and charts.

## Overview

Managing personal finances involves more than tracking income and expenses. Understanding spending habits and identifying where money goes can help people make better financial decisions.

This project aims to simplify that process by transforming raw financial transaction data into an interactive dashboard.

Users can upload their financial statements, organize transactions into categories, and explore summarized financial information through visualizations.

## Features

- **File Upload:** Import financial transactions from CSV and Excel files.
- **Data Processing:** Clean and process transaction data using Pandas.
- **Automatic Categorization:** Classify transactions based on previously registered keywords.
- **Custom Categories:** Create and manage personalized expense categories.
- **Interactive Tables:** Review and manually edit transaction categories.
- **Category Persistence:** Store category names and associated keywords in a JSON file.
- **Expense Analysis:** Calculate total expenses and summarize spending by category.
- **Data Visualization:** Explore expense distribution through interactive Plotly charts.
- **Income Tracking:** Review incoming payments and calculate total income.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive dashboard and user interface |
| Pandas | Data manipulation and processing |
| Plotly Express | Interactive data visualization |
| JSON | Category and keyword storage |

## Project Structure

```text
GestorFinanzas/
│
├── .streamlit/
│   └── config.toml
│
├── app/
│   ├── functions.py
│   ├── tables.py
│   └── styles.py
│
├── main.py
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Emerson-SM/GestorFinanzas.git
```

### 2. Navigate to the project directory

```bash
cd GestorFinanzas
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run main.py
```

The application will open in your default browser.

## Input Data Requirements

The application expects transaction files containing the following columns:

| Column | Description |
|---|---|
| Date | Transaction date |
| Details | Transaction description |
| Amount | Transaction amount |
| Debit/Credit | Transaction type (Debit or Credit) |

Supported file formats:

- CSV (`.csv`)
- Excel (`.xlsx`)
- Excel (`.xls`)

Dates are currently expected in the format `DD Mon YYYY`.

## Automatic Categorization

One of the main features of this project is its keyword-based categorization system.

When a user manually assigns a category to a transaction, the application can save its description as a keyword associated with that category.

When the same description appears in future transactions, the application can automatically assign the previously registered category.

This approach reduces repetitive manual classification and makes transaction management more efficient.

## Project Goals

This project was developed as part of my journey into data analytics, with the goal of strengthening practical skills in:

- Python programming.
- Data manipulation with Pandas.
- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA).
- Data visualization.
- Interactive dashboard development.
- Organizing and structuring Python applications.

## Future Improvements

Planned improvements include:

- Monthly income and expense analysis.
- Income versus expense comparisons.
- Spending trends over time.
- Budget management by category.
- Additional financial performance indicators.
- More advanced transaction categorization.
- Exporting processed transactions to CSV and Excel.

## Author

**Emerson Solano**

 Data Analyst | Python Developer

GitHub: [Emerson-SM](https://github.com/Emerson-SM)

---

*This project is continuously evolving as I explore data analytics, improve my programming skills, and implement new features.*
