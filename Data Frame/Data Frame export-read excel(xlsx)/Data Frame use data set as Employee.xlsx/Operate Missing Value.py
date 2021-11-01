import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Employee.xlsx",index_col="Name")
print(df.isnull()) #.isnull()-->if dont have data return value = True
print("")
print("")
print(df.isnull().any()) #.any()-->return true when find missing data
print("")
print("")
print(df.isnull().sum()) #find how many column that miss
print("")
print("")
print(df.notnull()) #.notnull()-->if dont have data return value = False
print("")
print("")
print(df.notnull().sum())
