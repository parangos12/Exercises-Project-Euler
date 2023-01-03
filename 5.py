counter=0
number=1
while counter!=20:
    for i in range(1,21):
        if number%i!=0:
            number+=1
            counter=0
            break
        else:
            counter+=1
    if counter==20:
        break
print(number)