# Sales Data Analysis using Python

## Overview
A beginner-friendly data analysis project that uses Python, Pandas, and Matplotlib to explore sample retail sales records.

## Questions explored
- What is the total revenue?
- Which product generated the most revenue?
- Which product had the most units sold?
- Which month generated the most revenue?
- How does revenue differ by product category?

## Tools
- Python
- Pandas
- Matplotlib
- CSV dataset

## Run the project (Windows / VS Code)
1. Install Python 3 if it is not already installed.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment (recommended):
   `py -m venv .venv`
5. Activate it in PowerShell:
   `.\.venv\Scripts\Activate.ps1`
   If activation is blocked, use Command Prompt or run the commands without activating the environment.
6. Install dependencies:
   `py -m pip install -r requirements.txt`
7. Run:
   `py analysis.py`

If `py` is not recognized, try `python` instead.

## Outputs
The program creates an `outputs` folder containing:
- `revenue_by_product.csv`
- `monthly_revenue.csv`
- `revenue_by_product.png`
- `monthly_revenue.png`

## Dataset note
The included dataset is a small, illustrative sample created for learning. It is not real company data. Be transparent about this in interviews.

## Resume bullet (use after you run and understand the project)
Built a Python-based sales data analysis project using Pandas to clean and aggregate retail sales records, calculate revenue and product-level performance, and visualize monthly trends with Matplotlib.
