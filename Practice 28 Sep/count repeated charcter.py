#count repeated characters in a string

n = "Towqeeeeeerrrr"
char = ''
rep = 1
for i in n:
    if n.count(i) > 1:
        rep = n.count(i)
        char = i
print(char,"comes",rep,'times')