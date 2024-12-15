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

df_IND = df[df['job_country'] == 'India']
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
- **SQL Dominance Across Roles:** *SQL* is the most sought-after skill across all three roles. It is particularly dominant in the *Data Engineer role, where `68%` of job postings mention it, followed closely by *Data Analyst role* at `52%`.

- **Python’s High Demand:** *Python* is a close contender, especially for *Data Scientists*, where it leads with `70%` of job postings requiring this skill. It also holds strong relevance for *Data Engineers* `61%` and *Data Analysts* `36%`.

- **Specialized Skills in Data Engineering:** *Data Engineering roles* emphasize cloud and big data technologies. Besides *SQL and Python*, there is significant demand for **Spark `38%`, AWS `37%`, and Azure `36%`**, reflecting the technical expertise required in this role.

- **Role-Specific Skill Trends:**
    - **Data Analysts:** Besides *SQL and Python*, traditional tools like *Excel* `35%` and data visualization tools like *Tableau `27%` and Power BI `21%`* are in demand, highlighting the analytical and reporting focus of this role.

    - **Data Scientists:** *R*, although not as dominant as Python or SQL, is still significant with `33%` of job postings mentioning it, underscoring its importance in statistical analysis and machine learning.

- **Power BI’s Limited Appeal:** *Power BI* shows the least demand among the listed skills, especially in *Data Analyst roles*, where only `21%` of job postings mention it.

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
![Likelihood of Skills Requested in the United States Job Postings](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Likelihood%20of%20Skills%20Requested%20in%20US%20Job%20Postings.png)


*Bar graph visualizing the top 3 data roles and their top 5 skills associated with each.*

### Insights Likelihood of Skills in US Job Postings:
- **Python Leads for Data Scientists:** In the U.S., *Python* is the most requested skill for *Data Scientists*, with `72%` of job postings highlighting it. This emphasizes Python's critical role in the data science domain.

- **SQL’s Consistency Across Roles:** *SQL* remains a foundational skill across all three roles. It is particularly crucial for *Data Engineers* `68%` and *Data Analysts* `51%`, indicating that strong database management skills are indispensable.

- **Excel’s Importance for Data Analysts:** *Excel* continues to be a highly demanded skill for *Data Analysts* in the U.S., with `41%` of job postings requiring it. This suggests that Excel remains a staple tool for data analysis and reporting.

- **Emerging Cloud Skills for Data Engineers:** In *Data Engineering roles*, cloud platforms such as *AWS* are in significant demand `43%`, along with *Azure* `32%`. This highlights the increasing importance of cloud computing skills in data engineering within the United States.

- **SAS and Tableau for Data Analysts:** For U.S. Data Analysts, tools like *SAS* `19%` and *Tableau* `28%` are also in demand, though not as prominent as SQL or Excel. Tableau’s demand suggests that data visualization skills are still crucial, though the competition with *Power BI* is evident.

### Comparison between both Graphs
- **SQL Dominance:** *SQL* is the top skill in both India and the U.S. across all roles. However, the demand for *SQL* is slightly higher in India, especially for *Data Engineers* `68%` compared to the U.S. This suggests a more uniform reliance on SQL in India, while in the U.S., there may be a broader distribution of skills.

- **Python’s Critical Role:** *Python* is highly demanded in both countries, particularly for *Data Scientists*. The demand is slightly higher in the U.S. `72%` compared to India `70%`, indicating its global importance in data science. However, Python’s demand for *Data Engineers* is slightly lower in India `61%` compared to the U.S. `65%`, highlighting its versatility.

- **Excel vs. Cloud Skills:** In the U.S., Excel remains crucial for *Data Analysts* `41%`, while cloud skills like *AWS* are more emphasized for *Data Engineers* `43%`. In India, *Excel* is also significant `35%`, but the demand for cloud skills like *Azure and AWS* is slightly lower. This reflects the U.S. market’s stronger focus on cloud technologies.

- **Tableau vs. Power BI:** *Tableau* is consistently in demand in both countries, especially for *Data Analysts*, with higher emphasis in the U.S. `28%` compared to India `27%`. *Power BI*, on the other hand, is gaining more traction in India `21%` compared to its absence in the U.S. charts, indicating regional preferences in data visualization tools.

- **R and SAS:** *R* is more relevant for *Data Scientists* in the U.S. `44%` compared to India`33%`, reflecting its specialized use in statistical analysis. *SAS* appears in the *U.S. Data Analyst* role `19%` but is absent in the Indian context, suggesting its niche application is more pronounced in the U.S.

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
- **SQL remains the most consistently demanded skill throughout the year**, holding the top position with over `50%` likelihood in job postings for most of the year. However, there is a gradual decline in its demand towards the end of the year, ending slightly above `45%`.

- **Excel shows a significant downward trend** throughout the year. It starts with a steady demand just above `40%` but experiences a noticeable decline from July onwards, dipping below `35%` by November before showing a sharp increase in December.

- **Tableau and Python exhibit similar demand levels**, with both skills remaining relatively stable between `25%` and `30%` throughout the year. *Python* initially has a slight edge, but *Tableau's* demand rises slightly towards the end of the year, matching Python's by December.

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
- **SQL remains the most consistently demanded skill** throughout the year, starting strong with `over 50%` likelihood in job postings. However, there is a slight decline in its demand towards the end of the year, `stabilizing at around 50%`.

- **Python and Excel show competitive demand**, with *Python* starting higher but *Excel* surpassing it in a few months. Both skills exhibit fluctuations, particularly in the middle of the year, but Excel maintains a slight upward trend, ending the year with similar demand as Python.

- **Tableau shows a steady demand pattern** throughout the year, though it generally remains lower than both *SQL and Python*. There is a notable decline in the latter half of the year, ending with `less than 30%` likelihood in job postings.

- **Power BI, though the least demanded skill** among the five, shows a significant upward trend from July onwards. It begins the year at a low point but consistently climbs, peaking in September and maintaining this elevated demand through to December.

### Comparison between both Line Graphs
- **Demand Trends**: *SQL* remains the top skill in both countries, but the U.S. shows a more noticeable decline in SQL and Excel demand towards the end of the year. In contrast, India maintains more consistent demand across the skills, with *Excel and Power BI* showing upward trends.

- **Skill Dynamics**: *Python and Tableau* show similar stability in both countries, but *Tableau* is more emphasized in the U.S., while *Power BI* is gaining traction in India. SAS in the U.S. remains a stable but less in-demand skill, reflecting its niche usage.

- **Market Dynamics**: The data suggests that while both markets value foundational skills like *SQL and Excel*, the U.S. is experiencing shifts in demand towards the end of the year, possibly reflecting changing industry needs or emerging trends. India, on the other hand, shows steadier demand with gradual growth in certain tools like *Power BI*.

## 3. How well do jobs and skills pay for Data Analysts?

To identify the highest-paying roles and skills, I only got jobs in the United States and looked at their median salary. But first I looked at the salary distributions of common data jobs like Data Scientist, Data Engineer, and Data Analyst, to get an idea of which jobs are paid the most.

View my notebook with detailed steps here: [4_Salary_Analysis](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/4_Salary_Analysis.ipynb).

### Visualise Data for Salary Distribution for United States
```python
sns.set_theme(style='ticks')

sns.boxplot(data=df_US_top6,
            x = 'salary_year_avg',
            y = 'job_title_short',
            order = job_order)
sns.despine()
plt.xlim(0, 600000)
plt.title("Salary Distribution of Data Jobs in the United States", fontsize=15)
plt.xlabel("Yearly Salary ($USD)")
plt.ylabel("")
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
plt.show()
```


### Result:
![Salary Distribution of Data Jobs in the United States](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Salary%20Distribution%20of%20data%20jobs%20in%20the%20United%20States.png)

*Box plot visualizing the salary distributions for the top 6 data job titles.* 

### Insights:
- **Senior Data Scientist roles command the highest salaries**, with the median salary hovering around `$200K` per year. The distribution also shows a wide range, with some individuals earning well above `$400K`, indicating that top-tier expertise in this field is highly rewarded.

- **Data Engineers and Senior Data Engineers have comparable salary ranges**, with medians close to `$150K`. However, Senior Data Engineers show a slightly broader range, with more outliers earning above `$300K`.

- **Data Scientists have a slightly lower median salary compared to Senior Data Scientists**, with the median around `$130K`. However, the range of salaries is wide, with some Data Scientists earning as much as or more than their senior counterparts, indicating opportunities for high pay depending on specific skills or company demand.

- **Data Analysts have the lowest median salary among the listed roles**, with a median around `$90K`. The salary distribution is narrower, with fewer high outliers, reflecting that this is typically an entry or mid-level role compared to the others.

## Investigate Median Salary Vs Skill for Data Analysts in United States
Next, I narrowed my analysis and focused only on data analyst roles. I looked at the highest-paid skills and the most in-demand skills. I used two bar charts to showcase these.

### Visualize Data
``` python
fig, ax = plt.subplots(2, 1)

sns.set_theme(style='ticks')

## Top 10 Highest Paid Skills for Data Analysts
sns.barplot(data=df_DA_top_pay,
            x='median',
            y='job_skills',
            hue='median',
            palette='dark:g_r',
            ax=ax[0],
            legend=False)
ax[0].set_title("Highest Paid Skills for Data Analyst in the US")
ax[0].set_ylabel("")
ax[0].set_xlabel("")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))

# Top 10 Most In-Demand Skills for Data Analysts')
sns.barplot(data=df_DA_skills,
            x='median',
            y='job_skills',
            hue='median',
            palette='light:g',
            ax=ax[1],
            legend=False)
ax[1].set_title("Most In-Demand Skills for Data Analyst in the US")
ax[1].set_ylabel("")
ax[1].set_xlabel("Median Salary ($USD)")
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
ax[1].set_xlim(ax[0].get_xlim())

fig.tight_layout()
plt.show()
```

### Results:
Here's the breakdown of the highest-paid & most in-demand skills for data analysts in the US:
![Highest Paid & Most In-Demand Skills for Data Analyst in the US](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Highest%20Paid%20%26%20Most%20In-Demand%20Skills%20for%20Data%20Analyst%20in%20the%20US.png)

*Two separate bar graphs visualizing the highest paid skills and most-in demand skills for data analysts in the US.*

### Insights:
- **Skill Value vs. Demand**: There is a noticeable distinction between the skills that command the highest pay and those that are most in demand. For example, *dplyr, Bitbucket, and GitLab* are among the highest-paid but do not appear on the most in-demand list. Conversely, *Python and Tableau* are highly in demand but offer slightly lower median salaries compared to niche skills.

- **Niche Skills Premium**: Specialized skills such as those related to *blockchain (Solidity), NLP (Hugging Face), and automation (Ansible)* are commanding higher salaries, possibly due to the lower supply of qualified professionals in these areas.

- **Core Skills Dominance**: Despite the rise of niche skills, core tools like *Python, SQL, and Tableau* remain in high demand, indicating that they are essential for Data Analysts across the industry.

- **Communication Tools**: The presence of *PowerPoint and Word* in the in-demand list highlights that effective communication and the ability to convey insights clearly are crucial components of a Data Analyst's role.

### Visualize for Salary Distribution for Globally.
``` python
sns.set_theme(style='ticks')

sns.boxplot(data=df_IND_job_titles,
            x='salary_year_avg',
            y='job_title_short',
            order=job_order)
sns.despine()
plt.xlim(0, 275000)
plt.title("Salary Distribution of Data Jobs in India", fontsize=15)
plt.xlabel("Yearly Salary ($USD)")
plt.ylabel("")
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
plt.show()
```
### Result:
![Salary Distribution of Data Jobs in India](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Salary%20Distribution%20of%20Data%20Jobs%20in%20India.png)

*Box plot visualizing the salary distributions for the top 6 data job titles.* 

### Insights:
- **Senior Data Scientist is the highest-paid role**, the median salary for Senior Data Scientists is significantly higher than other roles, around `$160K` per year, indicating that this position commands the highest compensation in the Indian data job market.

- **Data Engineers and Senior Data Engineers have comparable salaries**, the median salaries for these roles are relatively close, around `$150K` per year, suggesting that the seniority level within Data Engineering doesn't have a drastic impact on compensation.

- **Data Scientists have a slightly lower median salary than Senior Data Scientists**, the median salary is slightly lower than that of Senior Data Scientists, around `$130K` per year, indicating that experience and advanced skills are valued in this field.

- **Data Analysts have the lowest median salary**, as an entry or mid-level role, Data Analysts typically have lower salaries, around `$90K` per year, compared to the more senior positions, around `$100K` per year.

### Comparison between Salary Distribution between United States and India.
- *Senior Data Scientists* in the U.S., earns around `$400K`, have a much higher earning potential than their counterparts in India, earns around `$150K`, both in terms of median salary and upper-end outliers.

- *Data Scientists* in the U.S., earns around `$130K`, have a more substantial earning potential and a higher median salary compared to their Indian counterparts, earns around `$90K`.

- *Data Analysts* in the U.S., earns around `90K` more than those in India, earns around `50K`, with a higher median salary and greater earning potential at the top end.

- Across all data roles, the U.S. offers significantly higher salaries compared to India, both in terms of median and potential upper-end earnings.

- The disparity is most pronounced in senior roles, where U.S.-based professionals can earn up to twice as much as their Indian counterparts.

- While Indian data professionals are compensated well by local standards, the global market, particularly in the U.S., provides much more lucrative opportunities for similar roles.

## Investigate Median Salary Vs Skill for Data Analysts in Globally
Next, I narrowed my analysis and focused only on data analyst roles. I looked at the highest-paid skills and the most in-demand skills. I used two bar charts to showcase these.

*Note:*
*We excluded data from **India** because the number of data jobs with non-null values in `salary_year_avg` is very limited. Including this data could skew the analysis and lead to misleading conclusions.*

*We conducted our analysis using data from the global market to ensure more accurate and comprehensive insights.*

### Visualize Data
``` python
fig, ax = plt.subplots(2, 1)

sns.set_theme(style='ticks')

sns.barplot(data=df_DA_top_pay,
            x='median',
            y='job_skills',
            hue='median',
            palette='dark:g_r',
            ax=ax[0], 
            legend=False)
ax[0].set_title("Highest Paid Skills for Data Analyst Globally")
ax[0].set_xlabel("")
ax[0].set_ylabel("")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))

sns.barplot(data=df_DA_skills,
            x='median',
            y='job_skills',
            hue='median',
            palette='light:g',
            ax=ax[1],
            legend=False)
ax[1].set_title("Most In-Demand Skills for Data Analyst Globally")
ax[1].set_xlabel("Median Salary (&USD)")
ax[1].set_ylabel("")
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
ax[1].set_xlim(ax[0].get_xlim())

fig.tight_layout()
plt.show()
```
### Result:
Here's the breakdown of the highest-paid & most in-demand skills for data analysts globally:
![Highest Paid & Most In-Demand Skills for Data Analyst Globally](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Highest%20Paid%20%26%20Most%20In-Demand%20Skills%20for%20Data%20Analyst%20Globally.png)

*Two separate bar graphs visualizing the highest paid skills and most-in demand skills for data analysts globally.*

### Insights:
- **Niche Skills Premium**: Specialized skills like *svs, Solidity, dplyr, Bitbucket, and GitLab* command the highest salaries, likely due to their specialized nature and lower supply of skilled professionals.

- **Automation and Cloud Skills**: Skills related to automation *Ansible* and cloud platforms *Terraform, Couchbase* are also well-compensated.

- **Core Skills Dominance**: Essential tools like *Python, Tableau, SQL, and SQL Server* remain in high demand, indicating their fundamental importance in data analysis.

- **Data Visualization and Business Intelligence**: Tools like *Power BI, SAS, and Excel* are also highly sought-after, reflecting the need for effective data visualization and communication.

- **Communication Skills**: The presence of *PowerPoint and Word* in the in-demand list highlights the importance of effective communication and presentation skills for *Data Analysts*.

### Comparison between Highest Paid & Most In-Demand Skills for Data Analyst for US and Global.
- **Salary Disparity**: The global data analytics market offers significantly higher salaries for top-tier technical skills compared to the US market. This is particularly evident in niche skills like *svn and Solidity*.

- **In-Demand Skills**: Both globally and in the US, core data analysis tools like *Python, Tableau, and SQL* are consistently in high demand. However, the US market tends to offer slightly lower salaries for these in-demand skills compared to the global average.

- **Regional Variations**: The specific tools that are most highly valued and compensated can vary between regions. For example, *dplyr* is more highly regarded in the US compared to globally.

- **Skill Acquisition**: Given the higher salaries offered for specialized skills in the global market, individuals seeking to maximize their earning potential might consider acquiring niche skills that are in high demand.

- **Regional Considerations**: Data analysts considering relocation might want to research the specific tools and skills that are most valued and compensated in their desired region.

**Important Point:**
**Continuous Learning: The data analytics field is constantly evolving. Staying updated on the latest trends and technologies can help professionals remain competitive and increase their earning potential.**

## 4. What is the most optimal skill to learn for Data Analysts?
To identify the most optimal skills to learn ( the ones that are the highest paid and highest in demand) I calculated the percent of skill demand and the median salary of these skills. To easily identify which are the most optimal skills to learn.

View my notebook with detailed steps here: [5_Optimal_Skill](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/5_Optimal_Skill.ipynb).

### Visualize data for United States
``` python
from adjustText import adjust_text
from matplotlib.ticker import PercentFormatter

sns.set_theme(style='ticks')

sns.scatterplot(
    data= df_DA_skills_tech_high_demand,
    x='skill_percent',
    y='median_salary',
    hue='technology'
)
sns.despine()

# Set axis labels, title, and legend
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Yearly Salary')
plt.title('Most Optimal Skills for Data Analysts in the US')
plt.legend(title='Technology')

# Get current axes, set limits, and format axes
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K'))
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))

# Prepare texts for adjustText
texts = []
for i, txt in enumerate(df_DA_skills_tech_high_demand['skills']):
    texts.append(plt.text(df_DA_skills_tech_high_demand['skill_percent'].iloc[i], df_DA_skills_tech_high_demand['median_salary'].iloc[i], " " + txt))

# Adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'), force_text=(0.4))

# Adjust layout and display plot 
plt.tight_layout()
plt.show()
```
### Result
![Most Optimal Skills for Data Analysts in the US](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Most%20Optimal%20Skills%20for%20Data%20Analysts%20in%20the%20US.png)
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in the US.*

### Insights:
- **Programming Skills Premium**: As expected, programming skills (*Python, R, SAS*) tend to be associated with higher salaries, reflecting their importance in data analysis.

- **Database Expertise**: Skills related to databases (*Oracle, SQL Server*) are also valued, likely due to their critical role in data management and manipulation.

- **Analyst Tools**: While *Tableau and Power BI* are not as highly paid as programming or database skills, they are still in demand and offer competitive salaries, indicating their versatility in various data analysis tasks.

- **Soft Skills**: Skills like *PowerPoint, Excel, and Word* are essential for effective communication and presentation, but they might not be as directly tied to high salaries as technical skills.

- **Skill Combination**: The most successful data analysts might possess a combination of technical skills (programming, databases) and soft skills (communication, presentation) to maximize their earning potential.

### Visvalize data for India
``` python
from matplotlib.ticker import PercentFormatter
from adjustText import adjust_text

sns.set_theme(style='ticks')

sns.scatterplot(
    data = df_DA_skills_tech_high_demand,
    x = 'skill_percent',
    y = 'median_salary',
    hue='technology'
)
sns.despine()

# Add labels to the scatter points
texts = []
for i, txt in enumerate(df_DA_skills_tech_high_demand['skills']):
    texts.append(plt.text(df_DA_skills_tech_high_demand['skill_percent'].iloc[i], df_DA_skills_tech_high_demand['median_salary'].iloc[i], " " + txt))

# Adjust texts to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='grey'), force_text=(0.5, 0.5))

# Set axis labels, title, and legend
plt.title("Most Optimal Skills for Data Analysts in the India", fontsize=15)
plt.xlabel("Percent of Data Analyst Jobs")
plt.ylabel("Median Salary ($USD)")
plt.legend(title="Technology", loc='lower right')

# Get current axes, set limits, and format axes
ax = plt.gca()
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))

# Adjust layout and display plot
plt.tight_layout()
plt.show()
```

### Result
![Most Optimal Skills for Data Analysts in India](https://github.com/amitkr209/Python_Data_Project/blob/main/3_Project/Images/Most%20Optimal%20Skills%20for%20Data%20Analysts%20in%20the%20India.png)
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in India.*

### Insights:
- **Cloud and Big Data**: Skills related to cloud platforms (*Azure, AWS*) and big data technologies (*Spark*) are in high demand and offer competitive salaries in the Indian market.

- **Programming Basics**: *Python and R* are essential programming languages indicate a greater emphasis on foundational skills in the Indian market.

- **Data Visualization and Business Intelligence**: *Tableau and Power BI* are essential tools for data visualization and business intelligence, and their demand and salary indicating their universal value in the field.

- **Database Skills**: *Oracle and SQL* are still important for data management, but their salaries might be slightly lower.

- **Skill Combination**: A combination of technical skills (cloud, programming, databases) and soft skills (communication, presentation) is likely crucial for success in the Indian data analytics market.

### Comparisons between the scatter plots:
- **Salary Range**: The salaries in the US plot are generally higher than those in the India plot, indicating a wider range of earning potential for data analysts in the US.

- **Skill Emphasis**: The US plot emphasizes programming skills (*Python, R, SAS*) and database skills (*Oracle, SQL Server*) more than the India plot.

- **Cloud and Big Data**: Skills related to cloud platforms (*Azure, AWS*) and big data technologies (*Spark*) are more prominent in the India plot, suggesting a greater focus on these areas in the Indian market.

- **Skill Combination**: While the specific skills might vary, the importance of a combination of technical skills (programming, databases, cloud) and soft skills (communication, presentation) is consistent across both regions.

## What I Learned
Throughout this project, I deepened my understanding of the data analyst job market and enhanced my technical skills in Python, especially in data manipulation and visualization. Here are a few specific things I learned:

1. **Advanced Python Usage:**
- **Efficiency**: Leveraging Python libraries like *Pandas, Seaborn, and Matplotlib* significantly enhances data analysis capabilities.
- **Versatility**: These tools provide a robust toolkit for handling various data tasks, from data manipulation to visualization.

2. **Data Cleaning and Preparation:**
- **Accuracy**: Thorough data cleaning is essential to ensure the reliability of analysis results.
- **Time Efficiency**: Investing time in data preparation can save time and effort later in the analysis process.

3. **Strategic Skill Analysis:**
- **Market Alignment**: Understanding the demand for specific skills is crucial for making informed career decisions.
- **Skill Development**: Identifying high-demand skills can guide professional development efforts.

Overall, this project highlighted the importance of technical proficiency in Python and data handling skills, as well as the need for strategic career planning in the competitive data job market.

## Insights:
This project provided several general insights into the data job market for analysts:

- **Skill Demand and Salary Correlation**: The data clearly demonstrates a strong correlation between the demand for specific skills and the associated salaries. This suggests that investing time and effort into acquiring sought-after skills can significantly boost earning potential.

- **Dynamic Market Trends**: The job market for data analysts is constantly evolving, with new skills emerging and others becoming less relevant. Staying updated on industry trends and technological advancements is crucial to remain competitive and adaptable.

- **Economic Value of Skills**: Understanding the economic value of different skills can help data analysts make informed decisions about their career paths. Focusing on skills that are both in-demand and well-compensated can maximize earning potential and long-term career prospects.

- **Skill Acquisition**: Data analysts should continuously invest in their skill development, focusing on acquiring skills that are in high demand and offer competitive salaries.

- **Strategic Learning**: By understanding the economic value of different skills, data analysts can make strategic decisions about their learning path and career goals.

## Challenges I Faced
This project was not without its challenges, but it provided good learning opportunities:

- **Data Inconsistencies**: Handling missing or inconsistent data entries requires careful consideration and thorough data-cleaning techniques to ensure the integrity of the analysis.

- **Complex Data Visualization**: Designing effective visual representations of complex datasets was challenging but critical for conveying insights clearly and compellingly.

- **Balancing Breadth and Depth**: Deciding how deeply to dive into each analysis while maintaining a broad overview of the data landscape required constant balancing to ensure comprehensive coverage without getting lost in details.

## Conclusions
This exploration into the data analyst job market has been incredibly informative, highlighting the critical skills and trends that shape this evolving field. The insights I got enhance my understanding and provide actionable guidance for anyone looking to advance their career in data analytics. As the market continues to change, ongoing analysis will be essential to stay ahead in data analytics. This project is a good foundation for future explorations and underscores the importance of continuous learning and adaptation in the data field.