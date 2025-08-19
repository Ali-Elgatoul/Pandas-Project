import pandas as pd
df = pd.read_csv("Titanic.csv")

# Q1
survival_series = df["Survived"]

# Q2
print(df.tail(3))
print("Data type of Age column:", df["Age"].dtype)

# Q3
age_filter = df[df["Age"] > 30][["Name", "Age"]]
print(age_filter)

# Q4
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df[["Name", "FamilySize"]].head())

# Q5
df["Age"] = df["Age"].fillna(df["Age"].mean())
average_age_by_class = df.groupby("Pclass")["Age"].mean()
print("Average age by Pclass:\n", average_age_by_class)

# Q6
survival_rate_by_gender = df.groupby("Sex")["Survived"].mean()
print("Survival rate by gender:\n", survival_rate_by_gender)