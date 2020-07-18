import requests
import pandas as pd
import io

def get_data(option):
    """returns a pandas dataframe with data about Florida cases"""
    if option == "new and save":
        csv = requests.get("https://opendata.arcgis.com/datasets/37abda537d17458bae6677b8ab75fcb9_0.csv").content
        df = pd.read_csv(io.StringIO(csv.decode('utf-8')))
        df.to_csv("Resources/data.csv", index=False)
        return df 
    elif option == "new":
        csv = requests.get("https://opendata.arcgis.com/datasets/37abda537d17458bae6677b8ab75fcb9_0.csv").content
        return pd.read_csv(io.StringIO(csv.decode('utf-8')))
    elif option == "use old":
        return pd.read_csv("Resources/data.csv",index_col=False)


def get_hospitalized_data(option):
    """filters out hospitalizations"""
    df = get_data(option) 
    filt = df["Hospitalized"]=="YES"
    return df[filt]