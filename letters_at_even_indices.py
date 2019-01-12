# TODO : python program to print letters at even indices.

str = input("Enter the string\n")
a = []
counter = 0
for letter in str:
    if (counter % 2) == 0:
        a.append(letter)
    counter += 1
print("".join(a))

# use this alternate single line code to print letters at even indices
print(str[::2])