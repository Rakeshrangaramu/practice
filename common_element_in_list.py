# TODO:python program that takes two lists and returns True if they have at least one common member

a = int(input("enter the list range "))
b = []
c = []
for i in range(a):
    b.append(int(input()))
x = int(input("enter the list range "))
for j in range(x):
    c.append(int(input()))
if b[i] in c:
    print("true")
else:
    print("false")


