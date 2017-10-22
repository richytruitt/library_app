import pandas as pd 

students = []
 
df = pd.read_excel('files/students.xlsx', sheetname='Sheet1')

for i in df.index:
    students.append(df['Student Names'][i])

