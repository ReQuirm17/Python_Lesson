import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df2 = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df["total"] = df["Price"]*df["Amount"]
print(df.sum(axis=0)) #sum of int data axis=0(column(U-D) axis=1(rows(L-R)
print("")
print("")
print(df2.sum(axis=1))