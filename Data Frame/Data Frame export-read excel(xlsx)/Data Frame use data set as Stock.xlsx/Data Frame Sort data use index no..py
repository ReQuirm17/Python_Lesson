import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df.sort_index(inplace=True) #sort ตามลำดับ A-Z ก-ฮ 0-9 ///sort_index(ascending = False) ---> reverse sort

print(df)
