import pickle,super

n=int(input("Enter number :"))
with open("C:/Users/Anonymous/Desktop/Git/data.txt",'wb') as f:

    for i in range(n):
        name=input("Enter name : ")
        rollno=input("Enter roll no :")
        address=input("Enter address :")
        s=super.student(name,rollno,address)
        pickle.dump(s,f)
print('pickling done')
f.close()
