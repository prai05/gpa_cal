import csv
import pandas

grade_sum = 0
credit_sum = 0
pd = pandas.read_csv('grade_data2.csv', index_col=0)

with open('grade_data2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: 
        grade_sum += float(row['credit'])*float(row['grade'])
        credit_sum += int(row['credit'])

print(pd)
print("GPA: %0.4s"%float(grade_sum/credit_sum))