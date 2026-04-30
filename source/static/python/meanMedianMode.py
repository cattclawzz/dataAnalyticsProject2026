import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldb.csv")

meanMonthlyIncome = df['appeared'].mean()

medianMonthlyIncome = (df["githubRepo.created"] - df["appeared"]).dropna().median()

modeMonthlyIncome = df['compilesTo'].mode()[0]

print(f"Mean: {meanMonthlyIncome} \nMedian: {medianMonthlyIncome} \nMode: {modeMonthlyIncome}")

print(df[["githubRepo.created", "appeared"]].dropna().head(10))

diff = df.loc[df["githubRepo.created"].notna(), "githubRepo.created"] - df["appeared"]
print(diff)

print("-------------")

valid_diff = df["githubRepo.created"].notna() & df["appeared"].notna()
median_diff = (df.loc[valid_diff, "githubRepo.created"] - df.loc[valid_diff, "appeared"]).median()
print(median_diff)
print(valid_diff)