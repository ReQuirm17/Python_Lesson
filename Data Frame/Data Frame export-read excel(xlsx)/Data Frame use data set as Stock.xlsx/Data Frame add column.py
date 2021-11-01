import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df["delivery"] = 100
df["total"] = df["delivery"]+df["Price"]
print(df)