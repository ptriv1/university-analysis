import pandas as pd

df = pd.read_csv("world-universities.csv", header=None)
df.columns = ["country_code", "university_name", "website"]

print(df.head())