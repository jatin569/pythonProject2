#function to check whether a string is a pangram or not

def pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s:
            print("Its not a Pangram")
            break
    else:
        print("Its a pangram")
s=input("Enter string: ")
pangram(s)