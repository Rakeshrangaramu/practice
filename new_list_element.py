# TODO: python program to add new element to the list

a = int(input("enter the no. of elements\n"))
b = []
for element in range(a):
    c = input("enter the elements of the list\n")
    b.append(c)

d = input("Enter the new element to be added\n")
b.append(d)
print(b)