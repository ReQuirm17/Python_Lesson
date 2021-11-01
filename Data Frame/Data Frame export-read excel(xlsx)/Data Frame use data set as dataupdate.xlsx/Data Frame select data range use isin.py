import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")

a = df.loc[(df.Temperature.isin([18,20,25]))] #df.column.isin([value])
print(a)