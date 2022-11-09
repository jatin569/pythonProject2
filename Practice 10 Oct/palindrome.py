n=input("Please enter string:")
n1=''
for i in range(len(n)-1,-1,-1):
        n1=n1+n[i]
if n==n1:
    print("palindrome")
else:
    print("not palindrome")