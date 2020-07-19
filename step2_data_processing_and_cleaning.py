import step1_raw_data_collection as step1
import pandas as pd
import datetime as dt

def get_hospitalized_data(option="static"):
    """Summary: Filters out hospitalized patients and returns dataframe
    
    Parameters:
        option (string): which data set to get
        
            options include: 
                1. "api and save"
                    -- requests new data and then saves/replaces as csv file in Resources
                2. "api"
                    -- just requests new data from api
                3. "static"
                    -- reads data from Resources folder
                Default: defaults to "static" dataset

    Returns: dataframe with only hospitalized patients
    """
    df = step1.get_data(option) 
    filt = df["Hospitalized"]=="YES"
    return df[filt]

def get_df_with_datetime_and_formatted_column(option="default"):
    """adds datetime column and a formatted column that's easier to read"""
    if option == "main":
        df = step1.get_data()
    else:        
        df = get_hospitalized_data()

    # add datetime column from case1 column
    # drop time of day to be able to group based on date
    df['CaseDateTime'] = pd.to_datetime(df.loc[:,'Case1'],format='%Y/%m/%d %H:%M:%S')
    df["FormattedCaseDateTime"] = df.loc[:,"CaseDateTime"].dt.strftime("%m/%d/%Y")
    df.loc[:,"CaseDateTime"] = pd.to_datetime(df.loc[:,"FormattedCaseDateTime"],format='%m/%d/%Y')    
    return df

def get_hospitalizations_by_casedatetime(df = get_df_with_datetime_and_formatted_column()):
    """returns a grouped dataframe by case date and hospitalizations"""
    return df.groupby(by="CaseDateTime").count().reset_index()[['CaseDateTime',"Hospitalized"]]

def get_groups_before_and_after_opening_date(opening_date = dt.datetime(2020,5,4), day_delta = 30, opening_day_shift = 0):
    """returns two dataframes in a tuple (df1, df2) for groups before an after an opening_date"""
    df = get_df_with_datetime_and_formatted_column()
    
    opening_date += dt.timedelta(days=opening_day_shift)

    date_before = opening_date - dt.timedelta(days=day_delta)
    date_after = opening_date + dt.timedelta(days=day_delta)

    filt = ((df["CaseDateTime"]>=date_before) & (df["CaseDateTime"] < opening_date))
    before_grp_df = df[filt]

    filt = ((df["CaseDateTime"]>opening_date) & (df["CaseDateTime"] <= date_after))
    after_grp_df = df[filt]

    return (before_grp_df, after_grp_df)

def get_groups_by_casedatetime():
    """returns two dataframes in a tuple (df1,df2) that are grouped by casedate"""
    grp_before, grp_after = get_groups_before_and_after_opening_date()
    return (get_hospitalizations_by_casedatetime(grp_before),get_hospitalizations_by_casedatetime(grp_after))   

def get_groups(group_name = "CaseDateTime", opening_date = dt.datetime(2020,5,4), day_delta = 30, opening_day_shift = 0):
    df1, df2 = get_groups_before_and_after_opening_date(opening_date, day_delta, opening_day_shift)
    df1 = df1.groupby(by=group_name).count().reset_index()[[group_name,"Hospitalized"]] 
    df2 = df2.groupby(by=group_name).count().reset_index()[[group_name,"Hospitalized"]] 
    return (df1,df2)

def get_group(group_name="CaseDateTime",option="default"):
        
    if option == "main":
        df = get_df_with_datetime_and_formatted_column()
    elif option == "default":
        df=get_hospitalized_data()
    
    return df.groupby(by=group_name).count().reset_index()[[group_name,"Hospitalized"]].sort_values(by=group_name)

def get_top10_counties_by_percentage():
    df = get_hospitalized_data()
    return (get_group("County").set_index("County")/df["Hospitalized"].sum()*100).sort_values(by="Hospitalized",ascending=False).head(10).style.format({"Hospitalized":"{:.1f}%"})