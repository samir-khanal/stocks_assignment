from random import randint , choices
import csv
import pandas as pd
stocks=[
    {"name": "LEC","price":randint(1000,10000)},
    {"name": "HPPL","price":randint(1000,10000)},
    {"name": "MBJC","price":randint(1000,10000)},
    {"name": "GCIL","price":randint(1000,10000)},
    {"name": "MDB","price":randint(1000,10000)},
    {"name": "SHIVM","price":randint(1000,10000)},
    {"name": "CITY","price":randint(1000,10000)},
    {"name": "RADHI","price":randint(1000,10000)},
    {"name": "UPPER","price":randint(1000,10000)},
    {"name": "DOLTI","price":randint(1000,10000)},
]

with open("stock.csv","w", newline="") as csvfile:
    fieldnames=["name", "price"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(stocks)

# with open("stock.csv", "r") as file:
#     reader = csv.DictReader(file)

df = pd.read_csv("stock.csv")
print("main output:")
print(df)

#df['Can Buy'] = df['price'] <5000
#df['Can Buy'] = ["Yes" if price < 5000 else "No" for price in df['price']]
df['can buy'] = df['price'].apply(lambda price:"yes" if price< 5000 else "no")
df.to_csv("output.csv",index=False) 
print("\nupdated data:\n")
print(df)

selected_stock = choices(stocks)
print("\nRandomly Selected Stock:")
print(selected_stock)
