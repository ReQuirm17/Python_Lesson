import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")#.read_excel(file location,sheet name,encode,set index)
print(df.head()) #.head() head 5 rows
print("")
print("")
print(df.head(9))#.head() read 9 rows
print("")
print("")
print(df.tail()) #.tail() read last 5 rows
print("")
print("")
print(df.tail(3)) #.tail() read last 3 rows
print("")
print("")
print(df.sample()) #.sample() random n rows
print("")
print("")
print(df.describe()) #.describe() show stat value
print("")
print("")
print(df.shape) #.shape find(row,col) dimension
print("")
print("")
print(df.columns)#.columns search col
print("")
print("")
print(df.values)#.values read data as array
