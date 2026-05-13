import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldb.csv")

df = df[df["type"] == "pl"] #Filter out any non programming languages

df = df[["title", "country", "lineCommentToken", "compilesTo", "numberOfUsers", "appeared"]] #Filter out unused columns

df = df.dropna(subset=["country", "lineCommentToken"]) #Remove rows missing data

df.loc[df["country"].str.contains(" and |,"), "country"] = "Various" #Remove inconsistency caused multiple country values

df.to_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldbCleaned.csv", index=False)