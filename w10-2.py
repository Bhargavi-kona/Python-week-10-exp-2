import pandas as pd
df = pd.read_csv("data.csv")
sorted_df = df.sort_values(by="Name", ascending=True)
print("Sorted Data:", sorted_df)
print("\nFirst 3 rows:", df.iloc[:3])
print("\nSelected Columns:", df[["Name", "Marks"]])
