import pandas as pd

df = pd.read_csv("world-universities.csv", header=None)
df.columns = ["country_code", "university_name", "website"]

counts = df.groupby("country_code").size()
print(counts)