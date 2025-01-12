n = int(input("Enter a number"))
sum = 0
for i in range(1,n+1) :
    if  i==2 or i==3 :
        sum = sum + i
    if i%2 == 0 or i%3==0 or i==1 :
        sum = sum 
    else :
        sum = sum + i

print(sum)

