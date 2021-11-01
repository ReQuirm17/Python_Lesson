import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")
for idx, row in df.iterrows(): #iterrows() use for loop
    print("อุณหภูมิ = {} องศา ส่งผลให้เกิด {}".format(row.Temperature, row.Event))