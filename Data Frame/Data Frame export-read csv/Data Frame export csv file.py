import pandas as pd
#DataFrame.to_csv(location,attribute)
#location --> file position
#attribute header=save header of col
#attribute index = save index no.

import pandas as pd
products = [{"Name":"Mango","color":"yellow","price":50},
            {"Name":"apple","color":"red","price":40},
            {"Name":"coconut","color":"green","price":30}]
df = pd.DataFrame(products)
df.set_index(["Name"],inplace=True)

df.to_csv("products.csv",header=True,index=True) #df.to_csv("Name-location",header,index)