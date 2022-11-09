#check given word is palindrome or not

def palindrome(n):
    n1 = ''
    for i in range(len(n)-1,-1,-1):
        n1=n1+n[i]
    if n==n1:
       print("palindrome")
    else:
       print("not palindrome")
n=input("Please enter string:")
palindrome(n)