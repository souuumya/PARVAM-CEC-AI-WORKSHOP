# Pandas Library is used for creating DataFrames and Data Analysis

# Importing pandas
import pandas as pd


# -------------------- DataFrame Creation --------------------

data = {"Name": ["A", "B", "C", "D"], "Age": [20, 30, 40, 50]}
df1 = pd.DataFrame(data)
print("DataFrame from Dictionary:\n", df1)


# From List of Dictionaries
df2 = pd.DataFrame([
    {"Name": "Akshay", "Age": 24},
    {"Name": "Ajay", "Age": 23},
    {"Name": "Jay", "Age": 35},
])
print("\nDataFrame from List of Dictionaries:\n", df2)


# -------------------- Reading CSV --------------------

df3 = pd.read_csv("data.csv")
print("\nData from data.csv:\n", df3.head())
print("\nInfo:\n")
df3.info()


df = pd.read_csv("weather.csv")
print("\nWeather Data:\n", df.head())
print("\nInfo:\n")
df.info()
print("\nColumns:", df.columns)


# -------------------- Head & Tail --------------------

print("\nTop 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))


# -------------------- Column Selection --------------------

print("\nCities:\n", df["city"])
print("\nTemperature:\n", df["temp"])


# -------------------- Row Selection --------------------

print("\nRow with index 3:\n", df.loc[3])
print("\nUsing iloc:\n", df.iloc[0:1])


# -------------------- Conditional Filtering --------------------

print("\nTemp > 35.5:\n", df[df["temp"] > 35.5])

print("\nHumidity between 40 and 50:\n",
      df[(df["humidity"] > 40) & (df["humidity"] < 50)])


# -------------------- Update Column --------------------

df["humidity"] = df["humidity"] + 1
print("\nUpdated Humidity:\n", df)


# -------------------- Missing Values --------------------

print("\nMissing Values:\n", df.isnull())

# Fill missing values with 0
df.fillna(0, inplace=True)
print("\nAfter fillna:\n", df)


# -------------------- Statistics --------------------

print("\nDescribe:\n", df.describe())
print("\nMean Humidity:", df["humidity"].mean())
print("Sum Humidity:", df["humidity"].sum())


# -------------------- Sorting --------------------

print("\nSort by city:\n", df.sort_values("city"))
print("\nSort by temp:\n", df.sort_values("temp"))


# -------------------- GroupBy --------------------

data2 = {
    "Dept": ["Dev", "Dev", "QA", "Dev", "QA"],
    "Salary": [15000, 18000, 13000, 20000, 16000],
}
df4 = pd.DataFrame(data2)

print("\nGroupBy Dept (Sum):\n", df4.groupby("Dept").sum())


# -------------------- Unique & Value Counts --------------------

print("\nUnique Departments:", df4["Dept"].unique())
print("\nDepartment Counts:\n", df4["Dept"].value_counts())


# -------------------- Export to CSV --------------------

df4.to_csv("dept.csv", index=False)
print("\nData exported to dept.csv successfully!")