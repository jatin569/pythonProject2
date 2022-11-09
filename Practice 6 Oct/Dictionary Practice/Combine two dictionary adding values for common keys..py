dic1={'oil':20,'coffee':10,'water':20}
dic2={'tea':25,'soap':28,'coffee':15}
dic3=dict()
for key,val in dic1.items():
    if key in dic2:
        dic3[key]=val+dic2.get(key)
print(dic3)