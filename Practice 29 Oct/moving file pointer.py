file = open("C:/Users/Anonymous/Desktop/Vn2/practice.txt", 'r')
file.seek(5)
print(file.read())
print(file.tell())#The tell() method to return the current position of the file pointer from the beginning of the file.