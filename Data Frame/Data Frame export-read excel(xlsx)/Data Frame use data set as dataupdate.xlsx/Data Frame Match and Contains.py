import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\dataupdate.xlsx",
                   "weather",index_col="Day")
a = df.Event.str.match("ฝนตก") #if row col event = ฝนตก return True ///match("str ต้องเหมือนกันหมดถึงจะหาเจอ")
b = df[a]
c = df.Event.str.contains("ตก") #if row col event = เเดด return True ///match("strไม่ต้องเหมือนกันหมดขอเเค่เหมือนกันซักตัว")
d = df[c]
print(a)
print("")
print("")
print(b)
print("")
print("")
print(c)
print("")
print("")
print(d)
