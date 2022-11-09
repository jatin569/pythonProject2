import pickle,super
f= open(r"C:/Users/Anonymous/Desktop/Git/data.txt",'rb')
while True:
    try:
        obj=pickle.load(f)
        obj.show()
    except EOFError:
        print("Done")
        break