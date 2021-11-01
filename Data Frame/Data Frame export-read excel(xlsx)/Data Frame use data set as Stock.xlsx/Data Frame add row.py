import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df["delivery"] = 100
df["total"] = df["delivery"]+df["Price"]
cols = {"Category":"Group", "Amount":"Quantity", "total":"Summation"} #{new:old}
df.rename(columns=cols, inplace=True)#.rename(columns))
df.drop("delivery",axis=1,inplace=True) #.drop(col,axis=0(row)//1(column)


product = [["หูฟัง","อุปกรณ์คอม",400,20,500],
           ["สายชาร์จ","อุปกรณ์คอม",1400,20,500]
           ]
cols1 = ["Name", "Group", "Price", "Quantity", "Summation"]
newdf = pd.DataFrame(data=product,columns=cols1)
newdf.set_index("Name",inplace=True)
df=df.append(newdf)
print(df)
