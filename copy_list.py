# TODO :  python program to create a copy of a list.

a =int( input("enter the no. of elements in list"))
b = []
d = []
for element in range(a):
    c = input("enter the element\n")
    b.append(c)

for element in b:
    d.append(element)

print("Original list is: " ,b)
print("copied list is: " , d)
