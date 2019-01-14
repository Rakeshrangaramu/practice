# TODO:a program to sort the elements of a list in ascending order.

a = int(input("enter the list range "))
b = []
c = []
temp = 0
i = 0
for i in range(a):
    b.append(int(input()))

for i in range(len(b)):
    for j in range(i + 1, len(b)):

        if b[i] > b[j]:
           b[i], b[j] = b[j], b[i]

print(b)