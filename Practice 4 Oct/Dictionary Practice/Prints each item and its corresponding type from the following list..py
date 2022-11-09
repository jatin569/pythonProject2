#Prints each item and its corresponding type from the following list.
d={'name':'Jatin','id':123,'age':25,123:'one'}
for i in d:
    print(i,d.get(i),type(i))
