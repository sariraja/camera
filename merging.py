import pandas as pd
import numpy as np
import glob

glob.glob(r"C:\Users\admin\Downloads\sales.xlsx")
all_data = pd.DataFrame()
for f in glob.glob((r"C:\Users\admin\Downloads\sales.xlsx")):
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)
    all_data.describe()
all_data['date'] = pd.to_datetime(all_data['date'])
status = pd.read_excel(r"C:\Users\admin\Downloads\customer-status.xlsx")
status
all_data_st = pd.merge(all_data,status,how ='left')
all_data_st.head()
all_data_st[all_data_st["account number"]==737550].head()
all_data_st['status'].fillna('bronze',inplace=True)
all_data_st.head()
pd.__version__
all_data_st["status"] = all_data_st["status"].astype("category")
all_data_st.head()
all_data_st.dtypes
all_data_st.sort(columns=["status"]).head()
all_data_st["status"].cat.set_categories(["gold","sliver","bronze"],inplace=True)
all_data_st.sort(columns=["status"]).head()
all_data_st["status"].describe()
all_data_st.groupby(["status"])["quantity","unit price","ext Price"].mean()
all_data_st.groupby([""])
