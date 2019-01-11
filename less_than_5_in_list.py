# TODO: program that prints out all the elements of the list that are less than 5
a = int(input("enter the list range"))
b = []
for i in range(a):
    b.append(int(input()))
for i in b:
    if i < 5:
        print(i)