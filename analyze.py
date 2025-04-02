import pandas as pd

df_universities = pd.read_csv("world-universities.csv")
df_continents = pd.read_csv("continents2.csv")

df_merged = pd.merge(df_universities, df_continents, on="country_code", how="left")

print(df_merged.head())