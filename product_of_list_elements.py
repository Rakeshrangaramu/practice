# TODO:  python program to find the product of all the elements of a list.

a = int(input("enter the no. of elements in list\n"))
b = []
d = 1
for element in range(a):
    c = int(input("enter the element\n"))
    d = d*c
    b.append(c)

print(b)
print(d)