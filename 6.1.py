n = int(input("Enter a number "))
def add_ODD(n):
   sum = 0
   for i in range(1,n+1) :
    if i==1 or i%2!=0 :
        sum = sum + i
        
   return(sum)
print(add_ODD(n))
   
   
