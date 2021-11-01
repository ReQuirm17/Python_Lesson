import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Employee.xlsx",index_col="Name")
print(df)

select = 'Salary'

df[select] = df[select].fillna(df[select].mean()) #col Salary which is miss value insert it use mean
print(df)
print("")
print("")
df[select] = df[select].fillna(18000)
print(df)
print("")
print("")
df.fillna(method="pad",inplace=True) # ค่าก่อนหน้า 1 เเถว
print(df)
print("")
print("")
df.fillna(method="bfill",inplace=True)# ค่าต่อไป 1 เเถว
print(df)
print("")
print("")
df.dropna(subset=["Job","Salary"],inplace=True) #.dropna(subset=[col])
df.dropna(axis="columns",inplace=True)
print(df)












