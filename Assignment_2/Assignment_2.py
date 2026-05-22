import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load a CSV
FILE_PATH = 'Assignment_1/EmergencyTriageDataset_Reduced_GenderColumnCleaned.csv'
df = pd.read_csv(FILE_PATH)

COLUMN = 'Fio2'
VALID_MIN = 21
VALID_MAX = 100

print(f"=== Cleaning: {COLUMN} ===")
print(f"Unique values: {df[COLUMN].unique()[:15]}")
print(f"Dtype: {df[COLUMN].dtype}")
print()

# Step 1: Convert to numeric
df[COLUMN] = pd.to_numeric(df[COLUMN], errors='coerce')
print(f"After type conversion — NaNs: {df[COLUMN].isnull().sum()}")
print(df[COLUMN].describe())

# Step 2: Range filter
invalid = df[(df[COLUMN] < VALID_MIN) | (df[COLUMN] > VALID_MAX)]
print(f"Out-of-range values: {len(invalid)}")

df.loc[(df[COLUMN] < VALID_MIN) | (df[COLUMN] > VALID_MAX), COLUMN] = np.nan

# Step 3: Impute 
impute_value = df[COLUMN].median()
df[COLUMN] = df[COLUMN].fillna(impute_value)

print(f"\nAfter cleaning:")
print(df[COLUMN].describe())
print(f"NaNs remaining: {df[COLUMN].isnull().sum()}")

#Median was chosen because each patient could be in different environments.
#As a result, the mean pulls towards the higher end, and doesn't give a equivalent representation of most patients
#Thus, the median gives the most stable result, by taking from the middle 

# Extra Step - Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(df['Fio2'].dropna(), bins=13, edgecolor='black', color='steelblue')
axes[0].set_xlabel('Fio2 Score')
axes[0].set_ylabel('Count')
axes[0].set_title('Fio2 Distribution (after type conversion)')

axes[1].boxplot(df['Fio2'].dropna(), vert=False)
axes[1].set_xlabel('Fio2 Score')
axes[1].set_title('Fio2 Box Plot')

plt.tight_layout()
plt.savefig('fio2_distribution.png', dpi=100, bbox_inches='tight')
plt.show()
print("Plot saved as fio2_distribution.png")