import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Paralympic_Medal_Count.xlsx","Paralympic_Medal_Count",
                   index_col="Team/Npc")
df.to_csv("Paralympic_Medal.csv", header=True, index=True)
df.sort_index(inplace=True)
df.Gold.sort_index(inplace=True)
print(df)