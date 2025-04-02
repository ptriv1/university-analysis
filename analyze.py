import pandas as pd

df = pd.read_csv("world-universities.csv")

counts = df.groupby("country_code").size()
print(counts)