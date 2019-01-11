# TODO: program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

a = int(input("enter the list range "))
input('enter the list elements ')
b = []
c = []
for i in range(a):
    b.append(int(input()))
# print(set(b))    Even this method could be used
c.append(b[0])
for i in b:
    for j in c:
        if i not in c :
            c.append(i)

print(c)
