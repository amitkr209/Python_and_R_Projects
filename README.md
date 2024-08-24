# Overview
Welcome to my analysis of the data job market, focusing on data analyst roles. This project was created out of a desire to navigate and understand the job market more effectively. It delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts.

The data sourced from [Luke Barousse's Python Course](https://www.lukebarousse.com/python) which provides a foundation for my analysis, containing detailed information on job titles, salaries, locations, and essential skills. Through a series of Python scripts, I explore key questions such as the most demanded skills, salary trends, and the intersection of demand and salary in data analytics.

# The Questions
Below are the questions I want to answer in my project:

1. What are the skills most in demand for the top 3 most popular data roles?
2. How are in-demand skills trending for Data Analysts?
3. How well do jobs and skills pay for Data Analysts?
4. What are the optimal skills for data analysts to learn? (High Demand AND High Paying)

# Tools I Used
For my deep dive into the data analyst job market, I harnessed the power of several key tools:

- **Python**: The backbone of my analysis, allowing me to analyze the data and find critical insights.I also used the following Python libraries:
    - **Pandas Library**: This was used to analyze the data.
    - **Matplotlib Library**: I visualized the data.
    - **Seaborn Library**: Helped me create more advanced visuals.
- **Jupyter Notebooks**: The tool I used to run my Python scripts which let me easily include my notes and analysis.
- **Visual Studio Code**: My go-to for executing my Python scripts.
- **Git & GitHub**: Essential for version control and sharing my Python code and analysis, ensuring collaboration and project tracking.

# Data Preparation and Cleanup
This section outlines the steps taken to prepare the data for analysis, ensuring accuracy and usability.

## Import & Clean Up Data
I start by importing necessary libraries and loading the dataset, followed by initial data cleaning tasks to ensure data quality.

```python
# Importing the Libraries
from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Loading Dataset
dataset = load_dataset("lukebarousse/data_jobs")
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
```

## Filter US and India Jobs
To focus my analysis on the U.S. and India job market, I apply filters to the dataset, narrowing down to roles based in the United States and India.
```python
df_US = df[df['job_country'] == 'United States']

df_IND = df[df['job_country'] == 'United States']
```

# The Analysis
Each Jupyter notebook for this project aimed at investigating specific aspects of the data job market. Here’s how I approached each question:

## 1. What are the most demanded skills for the top 3 most popular data roles?
To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting.

View my notebook with detailed steps here: [2_Skill_Demand](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/2_Skill_Count.ipynb).

### Visualize Data for India
```python
fig, ax = plt.subplots(len(job_titles), 1)

sns.set_theme(style='ticks')

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_per[df_skills_per['job_title_short'] == job_title].head(5)
    sns.barplot(data=df_plot,
                x='skill_percentage',
                y='job_skills',
                ax = ax[i],
                hue='skill_count',
                palette='dark:b_r')
    ax[i].set_title(job_title)
    ax[i].set_xlabel('')
    ax[i].set_ylabel('')
    ax[i].legend().set_visible(False)
    ax[i].set_xlim(0, 75)

    # remove the x-axis tick labels for better readability
    if i != len(job_titles) - 1:
        ax[i].set_xticks([])

    # label the percentage on the bars
    for n, v in enumerate(df_plot['skill_percentage']):
        ax[i].text(v, n, f'{v: .0f}%', va='center')

fig.suptitle("Likelihood  of Skills Requested in India Job Postings", fontsize=15)
fig.tight_layout()
plt.show()
```

### Result:
![Likelihood of Skills Requested in the India Job Postings](https://github.com/amitkr209/Python_Data_Project/blob/main/Likelihood%20of%20Skills%20Requested%20in%20the%20India%20Job%20Postings.png)

*Bar graph visualizing the salary for the top 3 data roles and their top 5 skills associated with each.*

### Insights:
- **SQL** is the most requested skill for *Data Analysts* and *Data Engineer*, with it in over half the job postings for both roles. For *Data Scientist*, **Python** is the most sought-after skill, appearing in 70% of job postings.
- Data Engineers require more specialized technical skills **(AWS, Azure, Spark)** compared to Data Analysts and Data Scientists who are expected to be proficient in more general data management and analysis tools (Excel, Tableau).
- **Python** is a versatile skill, highly demanded across all three roles, but most prominently for *Data Scientists* (70%) and *Data Engineers* (61%).

### Visualize Data for United States
```python
fig, ax = plt.subplots(len(job_titles), 1)

sns.set_theme(style='ticks')

for i, job_title in enumerate(job_titles):
    df_plot = df_skill_perc[df_skill_perc['job_title_short'] == job_title].head(5)
    sns.barplot(data=df_plot,
                x='skill_percentage',
                y='job_skills',
                hue='skill_count',
                palette='dark:b_r',
                ax=ax[i],
                legend=False)
    sns.despine()
    ax[i].set_title(job_title)
    ax[i].set_xlabel('')
    ax[i].set_ylabel('')
    ax[i].set_xlim(0, 75)

    # # remove the x-axis tick labels for better readability
    if i != len(job_titles) - 1:
        ax[i].set_xticks([])

    # label the percentage on the bars
    for n, v in enumerate(df_plot['skill_percentage']):
        ax[i].text(v + 1, n, f'{v: .0f}%', va='center')

fig.suptitle("Likelihood of Skills Requested in US Job Postings", fontsize=15)
fig.tight_layout()
plt.show()
```

### Result:
![Likelihood of Skills Requested in the India Job Postings](https://github.com/amitkr209/Python_Data_Project/blob/main/Likelihood%20of%20Skills%20Requested%20in%20US%20Job%20Postings.png)


*Bar graph visualizing the salary for the top 3 data roles and their top 5 skills associated with each.*

### Insights:
- **SQL** is the most requested skill for *Data Analysts* and *Data Engineers*, with it in over half the job postings for both roles. For *Data Scientists*, **Python** is the most sought-after skill, appearing in 72% of job postings.
- *Data Engineers* require more specialized technical skills **(AWS, Azure, Spark)** compared to *Data Analysts* and *Data Scientists* who are expected to be proficient in more general data management and analysis tools (Excel, Tableau).
- **Python** is a versatile skill, highly demanded across all three roles, but most prominently for *Data Scientists* (72%) and Data Engineers (65%).
