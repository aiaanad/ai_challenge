# test_csv.py
import pandas as pd

df = pd.read_csv("data/train/train/_classes.csv")
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))
print("\nData types:")
print(df.dtypes)