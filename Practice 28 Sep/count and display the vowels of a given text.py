#count and display the vowels of a given text

n="Stringo"
l=['a','e','i','o','u','A','E','O','U','I']

for i in l:
    if i in n:
        print(i,n.count(i))


