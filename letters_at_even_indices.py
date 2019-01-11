# TODO : python program to print letters at even indices.

str = input("Enter the string\n")
a = []
counter = 0
for letter in str:
    if (counter % 2) != 0:
        str.replace('letter', '')
    else:
        a.append(letter)
    counter += 1
print("".join(a))
