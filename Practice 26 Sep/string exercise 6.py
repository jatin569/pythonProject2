#Exercise 5: Count all letters, digits, and special symbols from a given string

n=input("Enter string: ")
char=0
digit=0
symbol=0
for i in n:
    if i.isalpha():
        char=char+1
    elif i.isnumeric():
        digit=digit+1
    else:
        symbol=symbol+1
print("Char:",char)
print("Digits:",digit)
print("Symbol:",symbol)