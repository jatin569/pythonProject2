# that accepts a string and calculate the number of digits and letters

s = input("Enter string : ")
letters=0
digits=0
for i in s:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digits+=1
print("letters :",letters,'\nDigits :',digits)
