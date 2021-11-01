import pandas as pd
name = ['mango','apple','watermelon']
color = ['yellow','red','green']
price = [50,60,80]
names = pd.Series(name)
colors = pd.Series(color)
prices = pd.Series(price)

frame = {'name':names,'color':colors,'price':prices}
df = pd.DataFrame(frame)
print(df)