def triangular():

    t_numbers=[]

    c=0
    for i in range(0,3000000):
        for j in range(1,i+1):
            c=c+j
            if i==j:
                t_numbers.append(c)
                c=0

    divisores=[]
    for j in t_numbers:
        for i in range(1,3000000):
            if j%i==0:
                divisores.append(i)
        if len(divisores)<500:
            divisores=[]
        else:
            print("El primer numero en alcanzar 5 divisores es " + str(j))
            return len(divisores)

print(triangular())
        


