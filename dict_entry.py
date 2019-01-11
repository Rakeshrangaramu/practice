# TODO: a script that asks for users’ Name and USN as an input and saves it in a Dictionary with USN as the key and Name as the value.
#  Take 3 entries from the user before printing the dictionary.

my_dict={}
for i in range(3):
    name = input("enter the student's name")
    usn = input("enter the usn")
    my_dict[name] = usn
print(my_dict)