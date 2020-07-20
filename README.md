# Covid 19 Project
![](Images/covid19_title.png)
**Team Members:** Chika Ozodiegwu, Kelsey Wyatt, Libardo Lambrano, Kurt Pessa

[Google Doc with Project Info](https://docs.google.com/document/d/1eqhODgskdKG3WJYACiSXgGqDT9dvwouSgv8UbxjRPY0/edit?usp=sharing)

___

### Data set used:
**Florida COVID19 Case Line Data** from the Florida Department of Health Open Data. [Available Here](https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-case-line-data)

![](Images/florida_covid19_data.jpg)
___

### Research Question
> **“Has hospitalizations (#) in Florida changed since reopening?”**

### Process of Data Analysis
![](Images/data_process.png)
#### Step 1: Raw Data Collection

![](Images/steps_presentation/01_data_load.png)

<details><summary>Expand to view code</summary>
    
```
    import pandas as pd
    df = pd.read_csv("Resources/Florida_COVID19_Case_Line_Data.csv")
    df.head(3)
```
</details>

___

#### Step 2: Data Processiong & Data Cleaning

**Single group**

![](Images/steps_presentation/02_one_group.png)

<details><summary>Expand to view code</summary>
    
```
    #df = step2.get_hospitalized_data()
    #df = step2.get_df_with_datetime_and_formatted_column()
    #df = step2.get_hospitalizations_by_casedatetime()

    group_name = "Gender"
    #group_name = "Age_group"
    #group_name = "Travel_related"
    #group_name = "Jurisdiction"
    #group_name = "County"

    df = step2.get_group(group_name)

    df
```
</details>
<br/>

**Two groups: before and after opening**

![](Images/steps_presentation/03_two_groups.png)

<details><summary>Expand to view code</summary>
    
```
    #df1, df2 = step2.get_groups_before_and_after_opening_date()
    #df1, df2 = step2.get_groups_by_casedatetime()

    group_name = "Gender"
    #group_name = "Age_group"
    #group_name = "Travel_related"
    #group_name = "Jurisdiction"
    #group_name = "County"

    df1,df2 = step2.get_groups(group_name)

    #df
    pd.concat([df1,df2],axis=1)
```
</details>
<br/>

**CSV clean up**

![](Images/steps_presentation/04_clean_database.png)

<details><summary>Expand to view code</summary>
    
```
    total_cases_county = new_csv_data_df.groupby(by="County").count().reset_index().loc[:,["County","Case1"]]
    total_cases_county.rename(columns={"County": "County", "Case1": "Total Cases"})
```
</details>
<br/>

___

### Part 1: Six (6) Steps for Hypothesis Testing 

#### 1. Identify
- **Populations** (divide Hospitalization data in two groups of data):
    1. Prior to opening
    2. After opening  
* Decide on the **date**:
    * May 4th - restaurants opening to 25% capacity
    * June  (Miami opening beaches)
- Distribution:
    * Distribution

#### 2. State the hypotheses
- **H0**: There is no change in hospitalizations after Florida has reopened
- **H1**: There is a change in hospitalizations after Florida has reopened

#### 3. Characteristics of the comparison distribution
- Population means, standard deviations

#### 4. Critical values
- p = 0.05
- Our hypothesis is nondirectional so our hypothesis test is **two-tailed**

#### 5. Calculate

#### 6. Decide!

___

### Part 2: Visualizations

#### 1. Number of cases

![](Images/steps_presentation/05_number_cases.png)

<details><summary>Expand to view code</summary>
    
```
    Total_covid_cases = new_csv_data_df["ObjectId"].nunique()
    Total_covid_cases = pd.DataFrame({"Total Number of Cases": [Total_covid_cases]})
    Total_covid_cases
```
</details>
<br/>

#### 2. Total number of cases per county

![](Images/steps_presentation/06_number_cases_county_all.png)

<details><summary>Expand to view code</summary>

```
    #Total number of cases per county
    total_cases_county = new_csv_data_df.groupby(by="County").count().reset_index().loc[:,["County","Case1"]]
    total_cases_county.rename(columns={"County": "County", "Case1": "Total Cases"})

    #Total number of cases per county sorted
    total_cases_county = total_cases_county.sort_values('Case1',ascending=False)
    total_cases_county.head(20)

    #Bar chart for total cases per county
    total_cases_county.plot(kind='bar',x='County',y='Case1', title ="Total Cases per County", figsize=(15, 10), color="blue")

    plt.title("Total Cases per County")
    plt.xlabel("County")
    plt.ylabel("Number of Cases")
    plt.legend(["Number of Cases"])
    plt.show()
```
    
</details>
<br/>

#### 3. Top 10 counties with total cases

![](Images/steps_presentation/07_top_counties_all.png)

<details><summary>Expand to view code</summary>

```
    #Top 10 counties with total cases
    top10_county_cases = total_cases_county.sort_values(by="Case1",ascending=False).head(10)
    top10_county_cases["Rank"] = np.arange(1,11)
    top10_county_cases.set_index("Rank").style.format({"Case1":"{:,}"})

    #Bar chart for total cases for top 10 counties
    top10_county_cases.plot(kind='bar',x='County',y='Case1', title ="Total Cases for Top 10 Counties", figsize=(15, 10), color="blue")

    plt.title("Total Hospitalizations for Top 10 Counties")
    plt.xlabel("County")
    plt.ylabel("Number of Cases")
    plt.legend(["Number of Cases"])
    plt.show()
```
    
</details>
<br/>

#### 4. Top 10 counties trending view of total cases as a percentage of total (top 10)

![](Images/steps_presentation/07_top_counties_as_perc.png)

<details><summary>Expand to view code</summary>

```
code here
```
    
</details>
<br/>

#### 5. Total number of cases by gender 

![](Images/steps_presentation/08_cases_gender_all.png)

<details><summary>Expand to view code</summary>

```
    # Total number of cases by gender
    total_cases_gender = new_csv_data_df.groupby(by="Gender").count().reset_index().loc[:,["Gender","Case1"]]
    total_cases_gender.rename(columns={"Gender": "Gender", "Case1": "Total Cases"})

    # Pie chart for total number of cases by gender
    total_cases_gender = new_csv_data_df["Gender"].value_counts()

    colors=["pink", "blue", "green"]

    explode=[0.1,0.1,0.1]

    total_cases_gender.plot.pie(explode=explode,colors=colors, autopct="%1.1f%%", shadow=True, subplots=True, startangle=120);

    plt.title("Total Number of Cases in Males vs. Females")
```
    
</details>
<br/>

#### 6. Total of hospitalizations only

![](Images/steps_presentation/09_total_hospitalizations_only.png)

<details><summary>Expand to view code</summary>

```
    #Filter data to show only cases that include hospitalization
    filt = new_csv_data_df["Hospitalized"] == "YES"
    df = new_csv_data_df[filt]
    df
```
    
</details>
<br/>

#### 7. Percentage of hospitalizations by gender

![](Images/steps_presentation/10_male_female_dist.png)

<details><summary>Expand to view code</summary>

```
    # Calculate percentages male/female
    df = step2.get_df_with_datetime_and_formatted_column()
    filt = df['Gender']=='Male'
    df = df[filt]
    df = step2.get_hospitalizations_by_casedatetime(df)
    male_by_week = df.groupby(pd.Grouper(freq='W',key='CaseDateTime')).sum()

    df = step2.get_df_with_datetime_and_formatted_column()
    filt = df['Gender']=='Female'
    df = df[filt]
    df = step2.get_hospitalizations_by_casedatetime(df)
    female_by_week = df.groupby(pd.Grouper(freq='W',key='CaseDateTime')).sum()

    male_perc = male_by_week['Hospitalized']/(male_by_week['Hospitalized']+female_by_week['Hospitalized'])*100
    female_perc = female_by_week['Hospitalized']/(male_by_week['Hospitalized']+female_by_week['Hospitalized'])*100

    # Plot data 
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,6))
    p1 = plt.bar(male_perc.index,male_perc,width=5,label='male',alpha=0.5)
    p2 = plt.bar(female_perc.index,female_perc,bottom=male_perc,width=5,label='female',alpha=0.5)
    plt.hlines(y=50,xmin=male_perc.index[0],xmax=male_perc.index[-1],alpha=0.8)
    plt.ylabel('Scores')
    plt.legend(handles=[p1,p2])
    plt.show()
```
    
</details>
<br/>

#### 8. Percentage of hospitalizations by age group

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 9. Hospitalizations by case

![](Images/steps_presentation/11_hosp_by_case.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 10. Compare travel-related hospitalization to non-travelrelated cases

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 11. Percentage of hospitalization before shut down

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 12. Percentage of hospitalization during shut down

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 13. Percentage of hospitalization after reopening

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>

#### 14. Statistical testing between before and after reopening

![](Images/steps_presentation/##.png)

<details><summary>Expand to view code</summary>

```
    code here
```
    
</details>
<br/>




