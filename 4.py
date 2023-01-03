list=[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        number=str(i*j)
        numberb=number[::-1]
        if number==numberb:
            list.append(int(number))
print(max(list))          

