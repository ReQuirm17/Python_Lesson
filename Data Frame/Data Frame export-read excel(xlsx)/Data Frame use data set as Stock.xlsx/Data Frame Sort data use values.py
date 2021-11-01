import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df.sort_values("Price",inplace=True) #sort_values(col) min to max
print(df)