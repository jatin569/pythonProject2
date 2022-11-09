#capitalize first and last letters of each word of a given string

strng = "nothing is impossible in this world"
str1 = strng.split()
res=[]
for i in str1:
    x=i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res=" ".join(res)
print("New Strng:", res)
