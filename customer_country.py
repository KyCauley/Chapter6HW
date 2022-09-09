import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')
write1 = open('customer_country.csv','w')
csvfile2 = csv.writer(write1,delimiter=',')
count=0

write1.write('Full Name, Country' + '\n')

next(csvfile)

for record in csvfile:
    write1.write(record[1] + ' ' + record[2] + ', ' + record[4] + '\n')
    count=count+1

write1.write("Total Number of Customers: " + str(count-1))
write1.close()
infile.close()