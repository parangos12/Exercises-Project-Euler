def pitagoras():
    lista=[]
    lista_final=[]

    for i in range(1,10000):
        for j in range(1,10000):

            k=((i**2+j**2)**(1/2))

            if k.is_integer():

                lista.append(i)
                lista.append(j)
                lista.append(k)

    
    for z in range(0,len(lista),3):
        
        lista_final.append(lista[z:z+3])

    lista_numeros=[]  
    for p in range(0,len(lista_final)):
            if lista_final[p][0]+lista_final[p][1]+lista_final[p][-1]==1000:
                i=lista_final[p][0]
                j=lista_final[p][1]
                k=lista_final[p][-1]

                lista_numeros.append(i)
                lista_numeros.append(j)
                lista_numeros.append(k)
                
                
    return lista_numeros

print(pitagoras())




