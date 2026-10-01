import pandas as pd


# 1. LOAD DATA

data_ride = pd.read_csv("data/rides.csv", encoding="utf-16")


# 2. INSPECT DATA
print("- Inspect data : ")

print(data_ride.shape)
print(data_ride.columns)
print(data_ride.head())

print(data_ride.dtypes)
print(data_ride.isnull().sum())
data_ride.info()


# 3. DATA QUALITY CHECKS

print(data_ride[data_ride["distance"] <= 0])

print(data_ride[data_ride["price"] <= 0])

data_ride["ride_id"].duplicated().sum()