#accepts a string and calculate the number of upper case letters and lower case letters
def calculate(s):
    upper=0
    lower=0
    for i in s:
        if i.islower():
            lower+=1
        else:
            upper+=1
    print("upper case",upper,'\nlower case',lower)

s="JAtin DhiMan"
calculate(s)