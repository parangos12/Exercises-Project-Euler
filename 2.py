lista=[1,2]
sump=2
while lista[-1]<4000000:
    result=lista[-1]+lista[-2]
    lista.append(result)
    if result%2==0:
        sump=sump+result
print(sump)
