# =========================================================
# STUDENT PERFORMANCE ANALYSIS PROJECT
# Exploratory Data Analysis (EDA)
# =========================================================

# ---------------------------------------------------------
# IMPORTING LIBRARIES
# ---------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting visualization style
sns.set_style("whitegrid")

# =========================================================
# LOADING DATASET
# =========================================================

# Loading the student performance dataset
info = pd.read_csv("student_performance_dataset.csv")

# =========================================================
# DATA OVERVIEW
# =========================================================

# Displaying statistical summary of the dataset
a = info.describe()
print(a)

# Displaying dataset information
print("Dataset Information")
info.info()

# Checking for missing values
print("\nMissing Values")
print(info.isnull().sum())

# =========================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# =========================================================

# ---------------------------------------------------------
# 1. AGE VS EXAM SCORE
# ---------------------------------------------------------
# This analysis investigates whether student age
# has any noticeable relationship with exam performance.

plt.figure(figsize=(8,5))

sns.lineplot(
    data=info,
    x="age",
    y="exam_score",
    color="yellow",
    errorbar=None
)

plt.title("Age vs Exam Score")
plt.xlabel("Age")
plt.ylabel("Exam Score")
plt.grid()

# Insight:
# The graph helps visualize how exam scores vary across age groups.

plt.show()

# =========================================================
# 2. AGE VS PRODUCTIVITY SCORE
# =========================================================
# This analysis explores how student productivity
# changes with age.

plt.figure(figsize=(8,5))

sns.lineplot(
    data=info,
    x="age",
    y="productivity_score",
    errorbar=None
)

plt.title("Age vs Productivity Score")
plt.xlabel("Age")
plt.ylabel("Productivity Score")
plt.grid()

# Insight:
# This graph helps identify whether productivity
# tends to increase or decrease with age.

plt.show()

# =========================================================
# 3. STUDY HOURS VS EXAM SCORE
# =========================================================
# Regression analysis is used here to investigate whether
# study hours are associated with exam scores.

plt.figure(figsize=(8,5))

sns.regplot(
    data=info,
    x="study_hours",
    y="exam_score",
    scatter_kws={'alpha':0.1}
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()

# Insight:
# The regression line helps visualize the overall relationship
# between study time and academic performance.

plt.show()

# Calculating correlation coefficient
b = info["study_hours"].corr(info["exam_score"])

print("\nCorrelation Between Study Hours and Exam Score")
print(b)

# =========================================================
# 4. STUDY HOURS TREND ANALYSIS
# =========================================================
# This visualization provides another perspective on how
# study habits relate to exam performance.

plt.figure(figsize=(8,5))

sns.lineplot(
    data=info,
    x="study_hours",
    y="exam_score"
)

plt.title("Study Hours Trend vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid()

plt.show()

# =========================================================
# 5. SLEEP HOURS VS EXAM SCORE
# =========================================================
# This analysis investigates whether sleep duration
# is associated with student academic performance.

plt.figure(figsize=(8,5))

sns.boxplot(
    data=info,
    x="sleep_hours",
    y="exam_score"
)

plt.title("Sleep Hours vs Exam Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Exam Score")

# Insight:
# Boxplots help compare score distributions across
# different sleep durations.

plt.show()

# =========================================================
# 6. SOCIAL MEDIA HOURS VS PRODUCTIVITY SCORE
# =========================================================
# This analysis examines whether social media usage
# is associated with student productivity levels.

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=info,
    x="social_media_hours",
    y="productivity_score"
)

plt.title("Social Media Hours vs Productivity Score")
plt.xlabel("Social Media Hours")
plt.ylabel("Productivity Score")
plt.grid()

# Insight:
# The scatter plot helps identify any positive or negative
# relationship between social media use and productivity.

plt.show()

# =========================================================
# 7. BURNOUT LEVEL VS EXAM SCORE
# =========================================================
# This analysis investigates the relationship between
# burnout levels and academic performance.

plt.figure(figsize=(8,5))

sns.boxplot(
    data=info,
    x="burnout_level",
    y="exam_score"
)

plt.title("Burnout Level vs Exam Score")
plt.xlabel("Burnout Level")
plt.ylabel("Exam Score")

# Insight:
# This helps examine whether burnout levels
# are associated with student performance.

plt.show()

# =========================================================
# 8. PART-TIME JOB VS EXAM SCORE
# =========================================================
# This analysis compares academic performance between
# students with part-time jobs and those without.

plt.figure(figsize=(8,5))

sns.boxplot(
    data=info,
    x="part_time_job",
    y="exam_score"
)

plt.title("Part-Time Job vs Exam Score")
plt.xlabel("Part-Time Job")
plt.ylabel("Exam Score")

# Insight:
# This comparison helps examine whether balancing
# work and academics is associated with performance.

plt.show()

# =========================================================
# 9. EXAM SCORE DISTRIBUTION
# =========================================================
# Histogram analysis is used to observe the distribution
# of exam scores among students.

plt.figure(figsize=(8,5))

sns.histplot(
    data=info,
    x="exam_score",
    bins=25,
    kde=True
)

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")

# Insight:
# This visualization helps identify whether scores
# are approximately normally distributed or skewed.

plt.show()

# =========================================================
# 10. OVERALL CORRELATION HEATMAP
# =========================================================
# The heatmap visualizes correlations between all
# numerical variables in the dataset.

plt.figure(figsize=(12,8))

sns.heatmap(
    info.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Overall Correlation Heatmap")

# Insight:
# Strong positive correlations appear closer to 1,
# while strong negative correlations appear closer to -1.

plt.show()

# =========================================================
# PROJECT CONCLUSION
# =========================================================
# This project explored various behavioral and lifestyle
# factors that may be associated with student performance.
#
# Key analyses included:
# - Study habits
# - Sleep duration
# - Social media usage
# - Burnout levels
# - Productivity trends
#
# The project demonstrates the use of Exploratory Data
# Analysis (EDA) techniques for extracting meaningful
# insights from student data.
