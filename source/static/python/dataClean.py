import pandas as pd

def clean(data):

    df = pd.read_csv(data)

    df = df[df["type"] == "pl"] #Filter out any non programming languages

    df = df[["title", "country", "lineCommentToken", "compilesTo", "numberOfUsers", "appeared"]] #Filter out unused columns

    df = df.dropna(subset=["country", "lineCommentToken"]) #Remove rows missing data

    df.loc[df["country"].str.contains(" and |,"), "country"] = "Various" #Remove inconsistency caused multiple country values

    df.to_csv(r"source\static\python\pldbCleaned.csv", index=False)

clean(r"source\static\python\pldb.csv")