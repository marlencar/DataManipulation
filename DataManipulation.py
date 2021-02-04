import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/sarmelin/Documents/DemoDatasets/Lesson 3/SalaryGender.csv', delimiter=',')
salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])
print(df)                   #Print DataFrame
print(df.shape)             #Print Dimensionality Check
print(type(df))             #Print Type
print(df.iloc[0:3])         #Slice
print(df['Salary'].unique())#Unique Values
print(df['Salary'].values)  #Values of Column
print(df.mean())            #Mean Values of the DataFrame
print(df.median())          #Median of All Columns
print(df.mode(axis=1))