d={'a':10,'b':20,'c':50,'d':10}
l=[]
res=dict()
for keys,values in d.items():
    if values not in l:
        l.append(values)
        res[keys]=values
print(res)