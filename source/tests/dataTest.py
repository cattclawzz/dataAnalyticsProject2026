import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\pldb.csv")

x = list(df.filter(like="features.").columns)
print(x)