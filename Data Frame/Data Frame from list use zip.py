import pandas as pd
product1 = ["mango","apple","watermelon"] #col1
product2 = ["Yellow","red",'green']#col2
product3 = [50,60,80] #col3
cols = ["Name","color","price"]
datas = list(zip(product1,product2,product3)) #list(zip(data connect))
df = pd.DataFrame(datas,columns=cols)
print(df)
