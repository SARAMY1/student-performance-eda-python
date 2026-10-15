# Student Performance Analysis — Exploratory Data Analysis (EDA)

A Python data analysis project exploring relationships between students' academic performance, study habits, sleep, social media usage, burnout, productivity and part-time employment.

## About this project

This is an **exploratory** analysis, not a causal study. Charts and correlations describe patterns in the dataset; they do not establish that one factor causes another.

## Analyses

1. Age vs. exam score
2. Age vs. productivity score
3. Study hours vs. exam score (regression)
4. Study hours trend vs. exam score
5. Sleep hours vs. exam score
6. Social media hours vs. productivity score
7. Burnout level vs. exam score
8. Part-time job vs. exam score
9. Exam score distribution
10. Overall numeric correlation heatmap

## Tech stack

Python, NumPy, Pandas, Matplotlib and Seaborn.

## Running locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Place `student_performance_dataset.csv` in the same folder as `student_performance_analysis.py`, then run:

```bash
python student_performance_analysis.py
```

Each chart opens in a Matplotlib window. Close the window to continue to the next chart.

## Dataset

The analysis expects a CSV with these columns: `age`, `exam_score`, `productivity_score`, `study_hours`, `sleep_hours`, `social_media_hours`, `burnout_level`, and `part_time_job`.

The supplied dataset contains 5,000 student records and 21 variables. Check the dataset's provenance and permission for public redistribution before publishing it.

## Example finding

The Pearson correlation between `study_hours` and `exam_score` in the supplied dataset is approximately **−0.0012** — almost no *linear* association. This is a descriptive observation, not a causal conclusion.

## Code provenance

The analysis script retains the author's original 10-section EDA workflow, visualizations and educational comments. Minimal corrections address a Seaborn argument typo and make the descriptive-statistics and dataset-info outputs visible. Comments describing causal effects were clarified to refer to associations.

## Limitations

- Relationships are observational and potentially confounded.
- Some boxplots may be crowded if their x-axis has many distinct values.
- The correlation heatmap covers numeric variables only.
- This script does not train or validate a predictive model.
