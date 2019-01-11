#TODO:Given a element, search the entire list for the element and return the indices that match the list
b = []
a = int(input("enter the list range "))
for i in range(a):
    b.append(int(input()))
c = []
#
r = int(input("enter the element to be searched"))
index = 0
for element in b:
    if element == r:
        c.append(index)
    index += 1
print(c)
