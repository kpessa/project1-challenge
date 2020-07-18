import step1_rawdatacollection as step1
import pandas as pd

def get_hospitalized_data(option="use old"):
    """filters out hospitalizations"""
    df = step1.get_data(option) 
    filt = df["Hospitalized"]=="YES"
    return df[filt]

def get_df_with_datetime_and_formatted_column():
    df=get_hospitalized_data()
    # add datetime column from case1 column
    # drop time of day to be able to group based on date
    df['CaseDateTime'] = pd.to_datetime(df.loc[:,'Case1'],format='%Y/%m/%d %H:%M:%S')
    df["FormattedCaseDateTime"] = df.loc[:,"CaseDateTime"].dt.strftime("%m/%d/%Y")
    df.loc[:,"CaseDateTime"] = pd.to_datetime(df.loc[:,"FormattedCaseDateTime"],format='%m/%d/%Y')    
    return df

def get_grouped_hospitalizations_by_casedatetime():
    df = get_df_with_datetime_and_formatted_column()
    return df.groupby(by="CaseDateTime").count().reset_index()[['CaseDateTime',"Hospitalized"]]
