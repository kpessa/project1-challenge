import requests
import pandas as pd
import io

def get_data(option="static"):
    """Returns a pandas dataframe with data about Florida cases
    
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
    Returns:
        df (returns a dataframe of covid data)
    """
    if option == "api and save":
        csv = requests.get("https://opendata.arcgis.com/datasets/37abda537d17458bae6677b8ab75fcb9_0.csv").content
        df = pd.read_csv(io.StringIO(csv.decode('utf-8')))
        df.to_csv("Resources/data.csv", index=False)
        return df 
    elif option == "api":
        csv = requests.get("https://opendata.arcgis.com/datasets/37abda537d17458bae6677b8ab75fcb9_0.csv").content
        return pd.read_csv(io.StringIO(csv.decode('utf-8')))
    elif option == "static":
        return pd.read_csv("Resources/data.csv",index_col=False)