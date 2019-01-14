# TODO:  a program to find if a given element is present in a given list.

a = int(input("enter the no. of elements in list"))
b = []
c = []
for element in range(a):
    c = input("enter the element\n")
    b.append(c)
src = input("enter the element to be searched: ")
if src in b:
    print("true")
else:
    print("false")
