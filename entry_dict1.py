# TODO: a program to make a dictionary of Data of USN and Name.

my_dict={}
for i in range(3):
    name = input("enter the student's name")
    usn = input("enter the usn")
    my_dict[name] = usn
print(my_dict)