import csv
roll_num=int(input("Enter roll number: "))
name=input("Enter a name: ")
city=input("Enter city: ")
list=[]
list.append(roll_num)
list.append(name)
list.append(city)
with open("student1.csv","a")as b:
    writer=csv.writer(b)
    writer.writerows([list])
b.close()
print("The data has been appended")
