import csv
csv_col=['ROLL NO','NAME','PLACE']
dict_data=[{'ROLL NO':1,'NAME':'Basima','PLACE':'irumpupalam'},
           {'ROLL NO':2,'NAME':'Sneha','PLACE':'pulpalli'},
           {'ROLL NO':3,'NAME':'Ameera','PLACE':'muvattupuzha'},
           {'ROLL NO':4,'NAME':'ciyana','PLACE':'uganda'},
           {'ROLL NO':5,'NAME':'Mariya','PLACE':'japan'},
           {'ROLL NO':6,'NAME':'irfana','PLACE':'china'}]
csv_file="Names.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open(csv_file))
print("CSv file s dictionary:\n")
for row in data1:
    print(row)
