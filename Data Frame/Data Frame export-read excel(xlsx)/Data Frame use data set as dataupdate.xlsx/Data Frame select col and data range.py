import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")#.read_excel(file location,sheet name,encode,set index)
a = df.Temperature #select col Temperature
b = df.Temperature[1:4] #select row index 1-3 can set like a slice Series
print(a)
print("")
print("")
print(b)