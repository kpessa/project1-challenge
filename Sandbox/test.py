import step1_rawdatacollection as step1
import step2_dataprocessingandcleaning as step2

import pandas as pd

#df = step2.get_hospitalized_data()
df = step2.get_df_with_datetime_and_formatted_column()
#df = step2.get_grouped_hospitalizations_by_casedatetime()



print(df)
