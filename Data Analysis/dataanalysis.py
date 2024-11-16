import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

#display the first few rows of the data
print(df.head())

#Describe the data, get descriptive for all numerical column
print(df.describe())

#check for missing values in the data
mv = df.isnull().sum()
print("missing values in each column:\n", mv)

#calculate the average  of a column
avg = df['Age'].mean()
print(f"Average of age:{avg}")

#count the unique values of a column
uv = df['Age'].nunique()
print(f"Unique values in age column: {uv}")

#filter  the data based on a condition, eg- filter all empls from engineering dept
eng_emp = df[df['Department'] ==  'Engineering']
print(eng_emp)

#find the maximum, eg -  find the max salary in the data
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print('Highest salary employee:\n', max_salary_emp)

#find the  minimum, eg -  find the min salary in the data
min_salary = df['Salary'].min()
min_salary_emp = df[df['Salary'] == min_salary]
print('Lowest salary employee:\n', min_salary_emp)

#count the frequency  of a value in a column, eg - count the number of employees in each department
dep_count = df['Department'].value_counts()
print('Department count:\n', dep_count)

#groupby and aggregate, eg - group by department and find the average salary of each department
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)

#sort the data, eg - sort the data by salary in descending order
sorted = df.sort_values(by='Salary', ascending=False)
print(sorted)

#sort the  data, eg - sort the data by salary in ascending order
sorted1 = df.sort_values(by='Salary', ascending=True)
print(sorted1)

#adding  a new column, eg - add a new column 'Years of Experience' based on 'Age'
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if  x>=35 else 'Junior')
print('Data with experience column:\n',df)


#data visualization

#plot a pie chart
plt.figure(figsize=(8,6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Department Count')
plt.show()


#plot a bar chart
plt.figure(figsize=(8,6))
plt.bar(dep_count.index, dep_count.values)
plt.title('Department Count')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

#plot a histogram
plt.figure(figsize=(8,6))
plt.hist(df['Salary'], bins=10, edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

#plot a scatter plot
plt.figure(figsize=(8,6))
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

#data manipulation
#drop a column, eg - drop the 'Age' column
df = df.drop('Age', axis=1)
print(df)
