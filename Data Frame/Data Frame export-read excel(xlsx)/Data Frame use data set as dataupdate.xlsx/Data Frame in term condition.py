import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")
a = df[df.Temperature <= 20]
print(a)
b = df.loc[(df.Event=="ฝนตก") & (df.Temperature>=35)] #df.loc[(cond1) &//|| (cond2)]
c = df.loc[(df.Temperature == 18) | (df.Temperature == 20) | (df.Temperature == 25) | (df.Temperature == 35)]
print("")
print(b)
print("")
print("")
print(c)
