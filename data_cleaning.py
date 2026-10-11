import pandas as pd

# Load dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")

print(df.head())

print("\nRows:", len(df))
print("Columns:", len(df.columns))



print(df.info())

print(df.isnull().sum())




import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

print("Duplicates removed")
print("Missing values handled")




df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month_name()

df["Quarter"] = df["Order Date"].dt.quarter



df["Revenue"] = df["Sales"]

df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
) * 100




df["Profit Margin"] = (
    df["Profit"] /
    df["Sales"].replace(0, 1)
) * 100






df.to_csv(
    "clean_superstore.csv",
    index=False
)

print("Dataset saved")