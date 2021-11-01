import pandas as pd
df = pd.read_csv("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\csv\products.csv") #read_csv("file location)
cols = ['Name','price']
colsName = ['สินค้า', 'สี', 'ราคา']
df2 = pd.read_csv("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\csv\products.csv",
                  encoding="utf-8",usecols=cols) #read_csv("file location",encode,specific columns)
df3 = pd.read_csv("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\csv\products.csv",
                  encoding="utf-8",names=colsName) #read_csv("file location",encode,assign col name)
print(df)
print("")
print("")
print(df2)
print("")
print("")
print(df3)