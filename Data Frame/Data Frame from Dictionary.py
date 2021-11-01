import pandas as pd
products = [{"Name":"Mango","color":"yellow","price":50},
            {"Name":"apple","color":"red","price":40},
            {"Name":"coconut","color":"green","price":30}]
df = pd.DataFrame(products)
df.set_index(["Name"],inplace=True) #Set index="Name"/// save as too df
print(df)