#Beware set index columns
import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx")
df2 = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
rows = [0,3,12]
name = ['จาน','ทีวี','ยางลบ']

df.drop(rows,axis=0,inplace=True) #.drop(row,axis,)
df2.drop(name,axis=0,inplace=True) #.drop(row,axis,)
print(df)
print("")
print("")
print(df2)