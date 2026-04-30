import matplotlib.pyplot as plt
import pandas as pd

def smokingMortality():
    df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldb.csv")

    print([col for col in df.columns if "features." in col.lower()])
    print()

    corr = df["CigarettesSmokedPerDay"].corr(df["MortalityRates"])
    corr = round(corr, 2)
    print(corr)

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["CigarettesSmokedPerDay"],
        df["MortalityRates"],
        s=50,
        alpha=0.6
    )

    plt.title(f"Correlation Between Cigarettes Smoked and Mortality Rates (r = {corr})")
    plt.xlabel("Cigarettes Smoked Per Day")
    plt.ylabel("Mortality Rates")
    plt.tight_layout()
    plt.show()

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldb.csv")

# Select all feature columns
featureCols = [col for col in df.columns if "features." in col.lower()]

# Count True features per row by checking not NaN
df['num_true_features'] = df[featureCols].notna().sum(axis=1)

# Check the last few rows
print(df[['num_true_features'] + featureCols].tail())