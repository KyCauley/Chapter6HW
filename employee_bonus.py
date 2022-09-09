import csv

infile = open('EmployeePay.csv','r')

csvfile=csv.reader(infile,delimiter=',')

next(csvfile)

for record in csvfile:
    print("Student ID: ", record[0])
    print("Full Name: ", record[1]+" "+record[2])
    print("Salary: ", record[3])
    print("Bonus: ",record[4])

    input()