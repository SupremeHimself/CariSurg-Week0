import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

#1 - Load a CSV
FILE_PATH = 'EmergencyTriageDataset_Reduced_Dirty.csv'
df_raw = pd.read_csv(FILE_PATH)

#print(f"Dataset loaded: {df_raw.shape[0]} rows x {df_raw.shape[1]} columns")
#print(f"Columns: {list(df_raw.columns)}")

#2 - See unique values
print(df_raw['Gender'].unique())
print(f"\nTotal unique values: {df_raw["Gender"].nunique()}\n")

#3 - Count each value
print(df_raw["Gender"].value_counts())


gender_map = {
    "Male":     1,
    "MALE":     1,
    "1":        1,
    "Female":   0,
    "FEMALE":   0,
    "0":        0
    }

#4 - Remap values
df_raw["Gender_Clean"] = df_raw["Gender"].map(gender_map)

print("\n""===== AFTER CLEANING ===== ""\n")
print(df_raw["Gender_Clean"].value_counts())
print(f"Any NaN values? {df_raw["Gender_Clean"].isnull().sum()}\n")

#5 - Drop a column
df_raw = df_raw.drop(columns = ["Gender"])

#6 - Rename a column
df_raw = df_raw.rename(columns = {"Gender_Clean" : "Gender"})

#7 - Confirm the result
print("===== COLUMN 'Gender' AFTER CLEANING =====")
print(df_raw["Gender"].value_counts())
print(f"Data type: {df_raw["Gender"].dtype}\n")
print(df_raw.head())