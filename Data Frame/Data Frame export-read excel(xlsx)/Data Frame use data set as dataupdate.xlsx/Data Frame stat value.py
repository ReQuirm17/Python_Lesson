import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "score", index_col="Name")#.read_excel(file location,sheet name,encode,set index)
print(df)
print("")
print("")
print("average is", df.Score.mean()) #df.colname.stat_value()
print("max value is", df.Score.max())
print("min value is",df.Score.min())
print("count every data",df.Score.count())
print("standard deviration is",df.Score.std())
print("sum of data is",df.Score.sum())

