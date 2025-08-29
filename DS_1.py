import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# importing CSV file
df = pd.read_csv(r"modified_dataset.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.describe())


# manipulation of data -

# missing values identification -
print(df.isna().sum())

# duplicate values identification -
print(df.duplicated().sum())

# basic stats  on particular columns -
print(df["Salary"].mean())  # Average salary of employee
print(df["Experience"].median())  # Finding most experienced employee
print(df["Gender"].mode())  # finding employee dominance

# filltering to find employee where experience is >= 19
df_filtered = df[df["Experience"] >= 19]
print(df_filtered)

df_filtered = df[(df["Experience"] > 17) & (df["Salary"] > 50000)]
print(df_filtered)


# sorting for getting least experienced employee -
df_sorted = df.sort_values(by="Experience")
print(df_sorted)

# filling missing values -
#df["Age"].fillna(df["Age"].mean(), inplace = True)

# rename the column -
df.rename(columns = {"Age" : "Emp_Age"}, inplace = True)
print(df.head())

# Adding new column and fill with 10% of salary ass bonus -
df["Bonus"] = df["Salary"] * 0.10
print(df.head())


# replacing as experienced where bonus > 6000 and trainee where Bonus < 5000 -
df["Bonus"] = np.where(df["Bonus"] > 6000, "Experienced",
                             np.where(df["Bonus"] < 5000, "Trainee","Average"))
print(df[[ "Emp_Age","Gender", "Salary", "Experience", "Bonus"]].head())

# Visualisations on the data -

# Average salary of Employee department wise -
avg_salary_dept = df.groupby("Department")["Salary"].mean()

# Bar chart to check average salary department wise -
plt.bar(avg_salary_dept.index, avg_salary_dept.values, color="orange")
plt.title("Average Salary Department-wise")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Count of each Bonus_Label
bonus_counts = df["Bonus"].value_counts()

# Pie Chart to checkoy the dominance of experienced average and trainee in company -
plt.pie(bonus_counts, labels=bonus_counts.index, autopct="%1.1f%%")
plt.title("Experienced vs Trainee Distribution")
plt.show()

# scatter plot  to find relation between experience and salary -
plt.scatter(df["Experience"], df["Salary"], color="blue", alpha=0.6)

plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


# histogram to find how many employees are in low salary group and how many employees are in high salary group -
plt.hist(df["Salary"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Salary Distribution of Employees")
plt.xlabel("Salary")
plt.ylabel("Count of Employees")
plt.show()

# Gender wise experience distribution Gender / Department ke respect me salary comparison -
sns.boxplot(x="Gender", y="Experience", data=df)
plt.show()