# Step 1 : Extract

import pandas as pd
df = pd.read_csv('sales.csv')

# Step 2: Clean the data
#-> Remove $ and quotes
#-> Convert price to float

df['price'] = (df['price']
               .astype(str)
               .str.replace("$","",regex=False)
               .str.replace('"',"", regex=False)
               .astype(float))

# Step 3: Deduplicate (same Product + Price)

df = df.drop_duplicates(subset=['product_name','price'])

# Step 4 : Convert USD -> INR

USD_TO_INR = 83
df['price_inr'] = df['price'] * USD_TO_INR

# Step 5 : Save the Clean data to clean_sales.json

df.to_json("clean_sales.json",orient='records',indent=4)
print("The file clean_sales.json created successfully")