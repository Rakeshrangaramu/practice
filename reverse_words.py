# TODO:Program that asks the user for a phrase/sentence.
#      Print back to the user the same string, except with the words in backwards order.

str = input("enter the sentence\n")
b =[]
a = str.split()
b = a[::-1]
print('$'.join(b))