#remove spaces from a given string

# n=" jatin dhiman   "
# print(n.replace(' ',''))
st='print shah rukh salmankhan'
x=st.split()
print(x)
for i in x:
    if i.startswith('s'):
        print(i)
