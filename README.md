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
![Likelihood of Skills Requested in the India Job Postings](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Likelihood%20%20of%20Skills%20Requested%20in%20India%20Job%20Postings.png)

*Horizontal Bar graph visualizing the top 3 data roles and their top 5 skills associated with each.*

### Insights Likelihood of Skills in India Job Postings:
- **SQL Dominance Across Roles:** SQL is the most sought-after skill across all three roles. It is particularly dominant in the Data Engineer role, where `68%` of job postings mention it, followed closely by Data Analyst role at `52%`.

- **Python’s High Demand:** Python is a close contender, especially for Data Scientists, where it leads with `70%` of job postings requiring this skill. It also holds strong relevance for Data Engineers `61%` and Data Analysts `36%`.

- **Specialized Skills in Data Engineering:** Data Engineering roles emphasize cloud and big data technologies. Besides SQL and Python, there is significant demand for **Spark `38%`, AWS `37%`, and Azure `36%`**, reflecting the technical expertise required in this role.
- **Role-Specific Skill Trends:**
    - **Data Analysts:** Besides SQL and Python, traditional tools like Excel `35%` and data visualization tools like Tableau `27%` and Power BI `21%` are in demand, highlighting the analytical and reporting focus of this role.

    - **Data Scientists:** R, although not as dominant as Python or SQL, is still significant with `33%` of job postings mentioning it, underscoring its importance in statistical analysis and machine learning.

- **Power BI’s Limited Appeal:** Power BI shows the least demand among the listed skills, especially in Data Analyst roles, where only `21%` of job postings mention it.

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
![Likelihood of Skills Requested in the United States Job Postings](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Likelihood%20of%20Skills%20Requested%20in%20US%20Job%20Postings.png))


*Bar graph visualizing the top 3 data roles and their top 5 skills associated with each.*

### Insights Likelihood of Skills in US Job Postings:
- **Python Leads for Data Scientists:** In the U.S., Python is the most requested skill for Data Scientists, with `72%` of job postings highlighting it. This emphasizes Python's critical role in the data science domain.

- **SQL’s Consistency Across Roles:** SQL remains a foundational skill across all three roles. It is particularly crucial for Data Engineers `68%` and Data Analysts `51%`, indicating that strong database management skills are indispensable.

- **Excel’s Importance for Data Analysts:** Excel continues to be a highly demanded skill for Data Analysts in the U.S., with `41%` of job postings requiring it. This suggests that Excel remains a staple tool for data analysis and reporting.

- **Emerging Cloud Skills for Data Engineers:** In Data Engineering roles, cloud platforms such as *AWS* are in significant demand `43%`, along with *Azure* `32%`. This highlights the increasing importance of cloud computing skills in data engineering within the United States.

- **SAS and Tableau for Data Analysts:** For U.S. Data Analysts, tools like *SAS* `19%` and *Tableau* `28%` are also in demand, though not as prominent as SQL or Excel. Tableau’s demand suggests that data visualization skills are still crucial, though the competition with Power BI is evident.

### Comparison between both Graphs
- **SQL Dominance:** SQL is the top skill in both India and the U.S. across all roles. However, the demand for SQL is slightly higher in India, especially for Data Engineers `68%` compared to the U.S. This suggests a more uniform reliance on SQL in India, while in the U.S., there may be a broader distribution of skills.

- **Python’s Critical Role:** Python is highly demanded in both countries, particularly for Data Scientists. The demand is slightly higher in the U.S. `72%` compared to India `70%`, indicating its global importance in data science. However, Python’s demand for Data Engineers is slightly lower in India `61%` compared to the U.S. `65%`, highlighting its versatility.

- **Excel vs. Cloud Skills:** In the U.S., Excel remains crucial for Data Analysts `41%`, while cloud skills like AWS are more emphasized for Data Engineers `43%`. In India, Excel is also significant `35%`, but the demand for cloud skills like Azure and AWS is slightly lower. This reflects the U.S. market’s stronger focus on cloud technologies.

- **Tableau vs. Power BI:** Tableau is consistently in demand in both countries, especially for Data Analysts, with higher emphasis in the U.S. `28%` compared to India `27%`. Power BI, on the other hand, is gaining more traction in India `21%` compared to its absence in the U.S. charts, indicating regional preferences in data visualization tools.

- **R and SAS:** R is more relevant for Data Scientists in the U.S. `44%` compared to India`33%`, reflecting its specialized use in statistical analysis. SAS appears in the U.S. Data Analyst role `19%` but is absent in the Indian context, suggesting its niche application is more pronounced in the U.S.

## 2. How are in-demand skills trending for Data Analysts?
To find how skills are trending in 2023 for Data Analysts, I filtered data analyst positions and grouped the skills by the month of the job postings. This got me the top 5 skills of data analysts by month, showing how popular skills were throughout 2023.

View my notebook with detailed steps here: [3_Skills_Trends](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/3_Skills_Trends.ipynb).

### Visualize Data for United States
```python
from matplotlib.ticker import PercentFormatter

df_plot = df_DA_pivot_percent.iloc[:, :5]

sns.set_theme(style='ticks')

sns.lineplot(data=df_plot,
             dashes=False,
             palette='tab10')
sns.despine()
plt.title("Trending Top Skills for Data Analyst In the United States", fontsize=15)
plt.xlabel("2023")
plt.ylabel("Likelihood in Job Postings")
plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
plt.legend().remove()

# annotate the plot with the top 5 skills using plt.text()
# Also, # Adjust the y position slightly for each label to prevent overlap
for i in range(5):
    if df_plot.columns[i] == 'tableau':
        plt.text(11.2, df_plot.iloc[-1, i] + 1, df_plot.columns[i], ha='left')
    elif df_plot.columns[i] == 'python':
        plt.text(11.2, df_plot.iloc[-1, i] - 1, df_plot.columns[i], ha='left')
    else:
        plt.text(11.2, df_plot.iloc[-1, i], df_plot.columns[i], ha='left')

plt.show()
```
### Result:
![Trending Top Skills for Data Analyst In the United States](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Trending%20Top%20Skills%20for%20Data%20Analyst%20In%20the%20United%20States.png)

*Line graph visualizing the trending top skills for data analysts in the US in 2023.*

### Insights of Treding Top Skills in United States:
- **SQL remains the most consistently demanded skill throughout the year**, holding the top position with over 50% likelihood in job postings for most of the year. However, there is a gradual decline in its demand towards the end of the year, ending slightly above `45%`.

- **Excel shows a significant downward trend** throughout the year. It starts with a steady demand just above `40%` but experiences a noticeable decline from July onwards, dipping below `35%` by November before showing a sharp increase in December.

- **Tableau and Python exhibit similar demand levels**, with both skills remaining relatively stable between `25%` and `30%` throughout the year. Python initially has a slight edge, but Tableau's demand rises slightly towards the end of the year, matching Python's by December.

- **SAS, though consistently the least demanded skill** among the five, maintains a steady presence with a likelihood between `20%` and `25%` in job postings throughout the year. There is a slight increase in demand in December, aligning with the overall trend of skills gaining traction towards the year's end.

### Visualize Data for India
```python
from matplotlib.ticker import PercentFormatter

df_plot = df_DA_IND_percent.iloc[:, :5]

sns.set_theme(style='ticks')
sns.lineplot(data = df_plot,
             dashes = False,
             palette = 'tab10')
sns.despine()
plt.title("Treding Top Skills of Data Analyst in the India", fontsize=15)
plt.xlabel("2023")
plt.ylabel("Likelihood in Job Postings")
plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
plt.legend().remove()

# annotate the plot with the top 5 skills using plt.text()
for i in range(5):
    plt.text(11.2, df_plot.iloc[-1, i], df_plot.columns[i])
plt.show()
```
### Result:
![Trending Top Skills for Data Analyst in the India](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Treding%20Top%20Skills%20of%20Data%20Analyst%20in%20the%20India.png)

*Line graph visualizing the trending top skills for data analysts in the India in 2023.*

### Insights of Treding Top Skills in India:
- **SQL remains the most consistently demanded skill** throughout the year, starting strong with `over 50%` likelihood in job postings. However, there is a slight decline in its demand towards the end of the year, stabilizing at around 50%.

- **Python and Excel show competitive demand**, with Python starting higher but Excel surpassing it in a few months. Both skills exhibit fluctuations, particularly in the middle of the year, but Excel maintains a slight upward trend, ending the year with similar demand as Python.

- **Tableau shows a steady demand pattern** throughout the year, though it generally remains lower than both SQL and Python. There is a notable decline in the latter half of the year, ending with less than `30%` likelihood in job postings.

- **Power BI, though the least demanded skill** among the five, shows a significant upward trend from July onwards. It begins the year at a low point but consistently climbs, peaking in September and maintaining this elevated demand through to December.

### Comparison between both Line Graphs
- **Demand Trends**: SQL remains the top skill in both countries, but the U.S. shows a more noticeable decline in SQL and Excel demand towards the end of the year. In contrast, India maintains more consistent demand across the skills, with Excel and Power BI showing upward trends.

- **Skill Dynamics**: Python and Tableau show similar stability in both countries, but Tableau is more emphasized in the U.S., while Power BI is gaining traction in India. SAS in the U.S. remains a stable but less in-demand skill, reflecting its niche usage.

- **Market Dynamics**: The data suggests that while both markets value foundational skills like SQL and Excel, the U.S. is experiencing shifts in demand towards the end of the year, possibly reflecting changing industry needs or emerging trends. India, on the other hand, shows steadier demand with gradual growth in certain tools like Power BI.