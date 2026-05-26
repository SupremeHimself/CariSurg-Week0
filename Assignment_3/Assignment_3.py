import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#File Read
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
df = pd.read_csv(FILE_PATH)

# ===== All cleanings from Days 1 and 2 =====

# Gender
gender_map = {'Male': 1, 'MALE': 1, '1': 1, 'Female': 0, 'FEMALE': 0, '0': 0}
df['Gender'] = df['Gender'].map(gender_map)

# GCS
df['GCS'] = pd.to_numeric(df['GCS'], errors='coerce')
df.loc[(df['GCS'] < 3) | (df['GCS'] > 15), 'GCS'] = np.nan
df['GCS'] = df['GCS'].fillna(df['GCS'].median())

# SBP
df['SBP'] = pd.to_numeric(df['SBP'], errors='coerce')
df.loc[(df['SBP'] < 50) | (df['SBP'] > 250), 'SBP'] = np.nan
df['SBP'] = df['SBP'].fillna(df['SBP'].median())

# DBP
df['DBP'] = pd.to_numeric(df['DBP'], errors='coerce')
df.loc[(df['DBP'] < 30) | (df['DBP'] > 150), 'DBP'] = np.nan
df['DBP'] = df['DBP'].fillna(df['DBP'].median())

# Pulse
df['pulse'] = pd.to_numeric(df['pulse'], errors='coerce')
df.loc[(df['pulse'] < 20) | (df['pulse'] > 250), 'pulse'] = np.nan
df['pulse'] = df['pulse'].fillna(df['pulse'].median())

# Temp
def to_celsius(val):
    if pd.isnull(val): return np.nan
    s = str(val).strip()
    try:
        if s.endswith('C'): return float(s[:-1])
        elif s.endswith('F'): return (float(s[:-1]) - 32) * 5/9
        else: return float(s)
    except: return np.nan

df['Temp'] = df['Temp'].apply(to_celsius)
df.loc[(df['Temp'] < 32) | (df['Temp'] > 43), 'Temp'] = np.nan
df['Temp'] = df['Temp'].fillna(df['Temp'].median())

# RR
df['RR'] = pd.to_numeric(df['RR'], errors='coerce')
df.loc[(df['RR'] < 5) | (df['RR'] > 60), 'RR'] = np.nan
df['RR'] = df['RR'].fillna(df['RR'].median())

# FiO2
df['Fio2'] = pd.to_numeric(df['Fio2'], errors='coerce')
df['Fio2'] = df['Fio2'].fillna(df['Fio2'].median())  # 100% is clinically valid — no range filter

# MAP
df['MAP'] = pd.to_numeric(df['MAP'], errors='coerce')
df['MAP_Calc'] = (df['SBP'] + 2 * df['DBP']) / 3
df['MAP'] = df['MAP'].fillna(df['MAP_Calc'])
df = df.drop(columns=['MAP_Calc'])

print(f"Clean dataset: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Total NaNs remaining: {df.isnull().sum().sum()}")

#Exporting the file as a copy
# df.to_csv('Assignment_3/EmergencyTriageDataset_Reduced_AllCleaned.csv', index = False)
# print("\n""===== FINAL RESULT ===")
# print(df.head())

# ===== Assignment #3 =====

# PART 1 -- Histogram: fio2 distribution
fig, ax = plt.subplots(figsize=(8, 4))

ax.hist(df['Fio2'], bins=20, edgecolor='black', color='#66BB6A', alpha=0.8)

# Clinical reference zones
ax.axvspan(0, 21, alpha=0.08, color='blue', label='Hyperoxia (<21%)')
ax.axvspan(100, 200, alpha=0.08, color='red', label='Hypoxia (>100%)')
ax.axvline(x=21, color='blue', linestyle=':', linewidth=1)
ax.axvline(x=100, color='red', linestyle=':', linewidth=1)

ax.set_title('Fraction of Inspired Oxygen Distribution — Mercer General ED', fontsize=12)
ax.set_xlabel('Fraction of Inspired Oxygen (FiO2)')
ax.set_ylabel('Number of Patients')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('fio2_histogram.png', dpi=100, bbox_inches='tight')
plt.show()
print("Saved: fio2_histogram.png")

# 1. What is the clinical question this plot answers?
# What is the distribution of oxygen support requirements across each patient?

# 2. What type of plot is appropriate (histogram, scatter, bar, box)?
# A historgram because it shows the distribution of a continuous variable

# 3. What reference lines or annotations would add clinical meaning?
# The hyperoxia line shows that there is a deficit in the FiO2 distribution, while the hypoxia line shows that there is a surplus


# PART 2 -- Bar chart: mean heart rate per GCS score
fig, ax = plt.subplots(figsize=(10, 5))

gcs_groups = df.groupby('GCS')['pulse'].mean()
gcs_std = df.groupby('GCS')['pulse'].std()

ax.bar(gcs_groups.index, gcs_groups.values, yerr=gcs_std.values,capsize=4,color='#5C6BC0', edgecolor='black', alpha=0.8,label='Mean Heart Rate')

# Clinical GCS reference zones
ax.axvspan(2.5, 8.5, alpha=0.08, color='red', label='Severe (3–8)')
ax.axvspan(8.5, 12.5, alpha=0.08, color='orange', label='Moderate (9–12)')
ax.axvspan(12.5, 15.5, alpha=0.08, color='green', label='Mild (13–15)')

ax.set_title('Mean Heart Rate by Glasgow Coma Scale Score — Mercer General ED', fontsize=12)
ax.set_xlabel('Glasgow Coma Scale (GCS) Score')
ax.set_ylabel('Mean Heart Rate (bpm)')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('pulse_vs_gcs.png', dpi=100, bbox_inches='tight')
plt.show()
print("Saved: pulse_vs_gcs.png")

# 1. What is the clinical question this plot answers?
# Does the level of consciousness have any association with a patient's heart rate?

# 2. What type of plot is appropriate (histogram, scatter, bar, box)?
# A bar chart is appropriate here because GCS is an ordinal variable with discrete scores.
# The bar chart respects that discrete nature by treating each GCS score as a distinct group, while the error bars communicate the variability of heart rate within each group

# 3. What reference lines or annotations would add clinical meaning?
# The severe, moderate and mild show the ranges in which the consciousness is being affected
# To add onto this a Tachycardia/Bradycardia line would be useful to show the upper and lower bounds for heart rate