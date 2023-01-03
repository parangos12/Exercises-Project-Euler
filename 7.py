#FUNCION PARA DETERMINAR SI UN NUMERO ES PRIMO O NO
def prime(number):
    contador=0
    for i in range(2, number):
        if number % i == 0:
            contador += i
            break  
    if contador == 0:
        return True
    else:
        return False
        
counter=0
for i in range(2,1000000):
    if prime(i)==True:
        counter+=1
    if counter==10001:
        print(i)
        break
print(counter)