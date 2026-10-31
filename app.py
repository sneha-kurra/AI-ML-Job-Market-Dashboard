"""Basic Streamlit dashboard for synthetic AI/ML job market data."""

import pandas as pd
import streamlit as st


DATA_FILE = "data/ai_ml_jobs.csv"


@st.cache_data
def load_data():
    """Read job listings from the CSV file."""
    return pd.read_csv(DATA_FILE)


st.title("AI/ML Job Market Intelligence Dashboard")
st.info("SYNTHETIC DATA â€” created for educational purposes.")

try:
    jobs = load_data()
except FileNotFoundError:
    st.error(f"The dataset file was not found: {DATA_FILE}")
    st.stop()

if jobs.empty:
    st.warning("The dataset is empty. Add job listings to the CSV file and try again.")
    st.stop()

st.sidebar.header("Filters")

job_role = st.sidebar.selectbox(
    "Job role", ["All"] + sorted(jobs["job_title"].dropna().unique().tolist())
)
location = st.sidebar.selectbox(
    "Location", ["All"] + sorted(jobs["location"].dropna().unique().tolist())
)
experience_level = st.sidebar.selectbox(
    "Experience level",
    ["All"] + sorted(jobs["experience_level"].dropna().unique().tolist()),
)
employment_type = st.sidebar.selectbox(
    "Employment type",
    ["All"] + sorted(jobs["employment_type"].dropna().unique().tolist()),
)

filtered_jobs = jobs.copy()

if job_role != "All":
    filtered_jobs = filtered_jobs[filtered_jobs["job_title"] == job_role]
if location != "All":
    filtered_jobs = filtered_jobs[filtered_jobs["location"] == location]
if experience_level != "All":
    filtered_jobs = filtered_jobs[
        filtered_jobs["experience_level"] == experience_level
    ]
if employment_type != "All":
    filtered_jobs = filtered_jobs[
        filtered_jobs["employment_type"] == employment_type
    ]

average_salary = (
    (filtered_jobs["salary_min"] + filtered_jobs["salary_max"]) / 2
).mean()

metric_columns = st.columns(4)
metric_columns[0].metric("Total Jobs", f"{len(filtered_jobs):,}")
metric_columns[1].metric("Total Companies", f"{filtered_jobs['company'].nunique():,}")
metric_columns[2].metric("Total Job Roles", f"{filtered_jobs['job_title'].nunique():,}")
metric_columns[3].metric(
    "Average Salary", f"₹{average_salary:,.0f}" if pd.notna(average_salary) else "N/A"
)

chart_column, listings_column = st.columns([1, 2])

with chart_column:
    st.subheader("Job Distribution")
    if filtered_jobs.empty:
        st.info("No jobs match the selected filters. Try changing your filters.")
    else:
        st.vega_lite_chart(
            filtered_jobs,
            {
                "width": 280,
                "height": 280,
                "mark": {"type": "arc", "innerRadius": 60},
                "encoding": {
                    "theta": {"aggregate": "count", "type": "quantitative"},
                    "color": {"field": "job_title", "type": "nominal"},
                    "tooltip": [
                        {"field": "job_title", "type": "nominal"},
                        {
                            "aggregate": "count",
                            "type": "quantitative",
                            "title": "Jobs",
                        },
                    ],
                },
            },
            width="stretch",
        )

with listings_column:
    st.subheader("Job Listings")
    if filtered_jobs.empty:
        st.info("No jobs match the selected filters. Try changing your filters.")
    else:
        st.dataframe(filtered_jobs, width="stretch")

