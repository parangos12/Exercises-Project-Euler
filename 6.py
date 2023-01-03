sum=0
square=0
for i in range(1,101):
    sum+=i
    square+=i**2
print(sum**2-square)