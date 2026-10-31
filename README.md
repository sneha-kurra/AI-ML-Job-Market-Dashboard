# AI/ML Job Market Dashboard

An interactive dashboard for exploring AI/ML job-market data. It is built with Python, Pandas, Streamlit, and CSV data. The dashboard includes a job distribution donut chart rendered with Streamlit's chart support.

The listings in `data/ai_ml_jobs.csv` are synthetic and were created only for educational purposes. They are not real job-market data.

## Features

- Filter jobs by role, location, experience level, and employment type using the sidebar.
- View total jobs, total companies, total job roles, and average salary for the selected listings.
- Explore the Job Distribution donut chart and the Job Listings table.
- See helpful messages if the CSV file is missing, the dataset is empty, or no jobs match the selected filters.

## Run the dashboard

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The app also requires Streamlit, which is not currently listed in `requirements.txt`. Install it with:

```bash
pip install streamlit
```

Then start the dashboard from the project folder:

```bash
streamlit run app.py
```

OpenAI Codex was used as an AI coding assistant for vibe coding, development, testing, and improving the dashboard.
