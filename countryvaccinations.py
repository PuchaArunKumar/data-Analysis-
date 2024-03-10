import numpy as np
import pandas as pd 
df=pd.read_csv("country_vaccinations.csv")
df["Year"]=pd.to_datetime(df["date"]).dt.strftime("%Y")
df['Month(1-12)']=pd.to_datetime(df["date"]).dt.strftime("%m")
df['Day']=pd.to_datetime(df["date"]).dt.strftime("%d")
df['Month(jan-Dec)'] = pd.to_datetime(df["date"]).dt.strftime("%b")
df['month(january-december)'] = pd.to_datetime(df["date"]).dt.strftime("%B")
print(df)
c=0
for i in df.values:
    if (i[15]=='2021'):
        if (i[16]=='05'):
            c+=1
print("In May 2021, a total of",c,"people in india received vaccination")

