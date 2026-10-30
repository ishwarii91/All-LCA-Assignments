
import pandas as pd

file_name = input("Enter file name (.csv or .xls): ")

if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
elif file_name.endswith(".xls") or file_name.endswith(".xlsx"):
    df = pd.read_excel(file_name)
else:
    print("Invalid file format")
    exit()

print("\nOriginal Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df_drop = df.dropna()
print("\nDataset after removing missing values:")
print(df_drop)

df_fill = df.fillna("Unknown")
print("\nDataset after filling missing values:")
print(df_fill)

print("\nDuplicate Records:")
print(df.duplicated().sum())

df = df.drop_duplicates()
print("\nDataset after removing duplicates:")
print(df)

column_name = input("\nEnter column name to remove: ")

if column_name in df.columns:
    df = df.drop(column_name, axis=1)
    print("\nDataset after removing column:")
    print(df)

print("\nSelected Dataset:")
print(df.loc[:, :])

df.to_csv("preprocessed_data.csv", index=False)

print("\nPreprocessed dataset saved successfully!")
