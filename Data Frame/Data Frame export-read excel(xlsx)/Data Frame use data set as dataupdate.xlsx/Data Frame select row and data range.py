import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")
print(df)
a = df[0:3].Event #row 0-3 col event
b = df.loc["2020-12-02"]["Event"] #row 2020-12-02 col event
c = df.loc["2020-12-02":"2020-12-15"]["Event"]
print(a)
print("")
print("")
print(b)
print("")
print("")
print(c)