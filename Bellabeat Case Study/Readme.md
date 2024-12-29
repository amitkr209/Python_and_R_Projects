# Bellabeat Data Analysis Case Study

Welcome to the Bellabeat Data Analysis Case Study. This project focuses on analyzing trends in smart device usage and how these trends can inform Bellabeat’s marketing strategy. The primary goal is to derive actionable insights from data collected from Fitbit users to enhance customer engagement and product offerings.

## Blog: Explaining the Process

In my blog, I delve deeper into the process and methodology behind this case study. I discuss the significance of each step, from data cleaning to generating insights. This includes a breakdown of challenges, the rationale behind chosen techniques, and reflections on the outcomes. The blog is an educational resource for anyone interested in data analytics and R programming. [**Read the blog here**](https://medium.com/towards-data-engineering/bellabeat-analysis-0751cf917c91).

## The Questions

Below are the key business questions this project aims to address:

- What are some trends in smart device usage?
- How could these trends apply to Bellabeat customers?
- How could these trends help influence Bellabeat’s marketing strategy?

## Tools I Used

For this project, the following tools were utilized:

- **R and RStudio**: For data analysis and visualization.
- **Tidyverse**: Data manipulation and visualization.
- **Janitor**: Cleaning column names.
- **Lubridate**: Handling date-time formats.
- **Skimr**: Summarizing data.
- **Tableau**: For advanced data visualization and dashboarding.

## Data Preparation and Cleanup

This section outlines the steps taken to prepare the dataset for analysis:

### Import & Initial Inspection

1. **Load Necessary Libraries:**

    ```r
    library(tidyverse)
    library(janitor)
    library(lubridate)
    library(skimr)
    ```

2. **Import Datasets:**

    ```r
    daily_activity <- read.csv("dailyActivity_merged.csv")
    daily_sleep <- read.csv("sleepDay_merged.csv")
    weight_log <- read.csv("weightLogInfo_merged.csv")
    ```

3. **Inspect Data Structure:**

    ```r
    str(daily_activity)
    str(daily_sleep)
    str(weight_log)
    ```

### Data Cleaning

1. **Standardized Column Names:**

    ```r
    daily_activity <- clean_names(daily_activity)
    daily_sleep <- clean_names(daily_sleep)
    weight_log <- clean_names(weight_log)
    ```

2. **Formatted Date Columns:**

    ```r
    daily_activity$activity_date <- as.Date(daily_activity$activity_date, '%m/%d/%y')
    daily_sleep$sleep_day <- as.Date(daily_sleep$sleep_day, '%m/%d/%y')
    weight_log$date <- parse_date_time(weight_log$date, '%m/%d/%y %H:%M:%S %p')
    ```

3. **Removed Redundant Columns:**

    ```r
    weight_log <- weight_log %>% select(-c(fat))
    ```

4. **Added Calculated Columns:**

    ```r
    daily_activity$total_active_hours <- round((daily_activity$very_active_minutes + daily_activity$fairly_active_minutes + daily_activity$lightly_active_minutes)/60, 2)
    daily_activity$sedentary_hours <- round(daily_activity$sedentary_minutes / 60, 2)
    daily_sleep$hours_in_bed <- round(daily_sleep$total_time_in_bed / 60, 2)
    daily_sleep$hours_asleep <- round(daily_sleep$total_minutes_asleep / 60, 2)
    ```

5. **Categorized BMI Values:**

    ```r
    weight_log <- weight_log %>% 
        mutate(bmi2 = case_when(
            bmi > 24.9 ~ 'Overweight',
            bmi < 18.5 ~ 'Underweight',
            TRUE ~ 'Healthy'))
    ```

6. **Filtered Outliers:**

    ```r
    daily_activity_cleaned <- daily_activity %>% 
        filter(calories > 0 & total_active_hours > 0)
    ```

## The Analysis

### Key Questions Explored

- **What are the average daily metrics for users?**
    - Average steps: 8319
    - Average sedentary hours: 15.87
    - Average very active minutes: 23.21
    - Average hours asleep: 6.99

- **Which days are users most active?**
    - Sundays showed the highest activity levels.

- **What is the relationship between activity metrics and calories burned?**
    - Positive correlations between calories burned and total active hours, as well as total steps.

- **How does weight relate to activity levels?**
    - Users around 60kg and 85kg appeared to be the most active.

### Visualizations

Created several ggplot visualizations and Tableau dashboards to showcase:

- Daily activity patterns.
- Relationship between steps, activity hours, and calories burned.
- Weight and activity correlations.

## Insights

### User Behavior Trends:

- Many users fall short of recommended activity and sleep guidelines.
- Sundays are the most active days, with a decline in activity levels throughout the week.

### Potential Recommendations for Bellabeat:

- Highlight the importance of consistent activity and adequate sleep in marketing campaigns.
- Develop features that motivate users to maintain activity levels during weekdays.

### Marketing Strategy Enhancements:

- Create content around optimal health practices tailored to user habits.
- Introduce gamification elements to encourage meeting daily activity goals.

## Challenges Faced

- **Data Gaps**: Limited data on certain metrics such as weight entries.
- **Outlier Handling**: Some data points required careful filtering to maintain analysis integrity.
- **Visualization Complexity**: Balancing clarity and depth in visualizations was critical.

## Conclusions

This analysis provides actionable insights into user behavior patterns and potential strategies for Bellabeat to enhance customer engagement. By leveraging these findings, Bellabeat can create a more impactful marketing approach and refine product offerings to better meet user needs.

Future studies could explore a larger dataset or integrate additional user demographics for a more comprehensive understanding of behavior trends.
