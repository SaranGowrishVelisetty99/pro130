import pandas as pd
import csv

df = pd.read_csv("data4.csv")


del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

print(df.shape)
print(list(df))

df.to_csv('main.csv') 