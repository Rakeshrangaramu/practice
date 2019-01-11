# TODO: python program to print a string in multiple lines

str = input("Enter the String \n")
a = str.split()
for element in a:
    print(" ".join(element))
