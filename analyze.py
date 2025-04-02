import pandas as pd

df_universities = pd.read_csv("world-universities.csv")
df_continents = pd.read_csv("continents2.csv")

df_merged = pd.merge(df_universities, df_continents, on="country_code", how="left")

missing = df_merged[df_merged["region"].isna()]

# Save to a CSV file
missing.to_csv("unmatched_country_codes.csv", index=False)

print("Unmatched entries saved to unmatched_country_codes.csv")