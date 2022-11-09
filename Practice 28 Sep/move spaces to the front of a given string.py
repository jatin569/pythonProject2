#move spaces to the front of a given string
n="jatin dhiman is "

n1=""
n2=''
for i in n:
    if i==" ":
        n1=n1+i
        continue
    else:
        n2=n2+i
print("string with spaces",n1+n2)
