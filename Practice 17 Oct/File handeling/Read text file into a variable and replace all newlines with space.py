# Read text file into a variable and replace all newlines with space

file=open('C:/Users/Anonymous/Desktop/geek.txt','r')
data = file.read().replace('\n', ' ')
print(data)


with open("C:/Users/Anonymous/Desktop/geek.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)