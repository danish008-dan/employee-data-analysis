# employee-data-analysis
This project performs Exploratory Data Analysis (EDA) on an employee dataset using Python (Pandas, NumPy, Matplotlib, Seaborn).

Employee Data Analysis Project
Project Overview

This project demonstrates data analysis and visualization using Python with the libraries Pandas, NumPy, Matplotlib, and Seaborn.
The dataset modified_dataset.csv contains information about employees, including:

Name

Age

Gender

Department

Experience (in years)

Salary

The main objectives of this project are:

Cleaning and manipulating employee data.

Performing statistical analysis on various columns.

Visualizing insights like department-wise salary, experience vs salary, and employee distribution based on bonus.

Dataset

The dataset contains the following columns:

Column	Description
Name	Employee Name
Age	Employee Age
Gender	Male/Female
Department	Department Name
Experience	Years of Experience
Salary	Monthly Salary in USD

Sample of the dataset:

   Name  Age  Gender Department  Experience  Salary
0  John   28    Male      IT           5    40000
1  Jane   32  Female      HR          10    55000
2  Mike   40    Male      IT          18    75000

Key Steps in the Project

Data Import & Exploration

Import CSV file using pandas.read_csv().

Check the first few rows (head()) and last few rows (tail()).

Check missing values (isna().sum()), duplicates (duplicated().sum()), and basic statistics (describe()).

Data Cleaning & Manipulation

Rename Age column to Emp_Age.

Filter employees based on experience and salary.

Sort employees by experience to find least experienced employees.

Fill missing values (if any).

Add a new column Bonus (10% of salary) and categorize as Trainee, Average, or Experienced.

Statistical Analysis

Average salary per department.

Median experience.

Mode of gender distribution.

Data Visualization

Bar chart: Department-wise average salary.

Pie chart: Employee distribution by bonus category (Trainee, Average, Experienced).

Scatter plot: Experience vs Salary.

Histogram: Salary distribution of employees.

Boxplot: Gender-wise experience distribution.

Required Libraries
pip install pandas numpy matplotlib seaborn

Sample Visuals
1. Department-wise Average Salary

2. Bonus Distribution (Experienced, Average, Trainee)

3. Salary vs Experience

4. Salary Distribution of Employees

5. Gender-wise Experience Distribution

Note: Replace the above URLs with actual images of your plots stored in the repo folder like /images/

How to Run the Project

Clone the repository:

git clone https://github.com/your-username/employee-data-analysis.git


Navigate to the project folder:

cd employee-data-analysis


Run the script:

python employee_analysis.py


All visualizations will be displayed and can be saved locally.
