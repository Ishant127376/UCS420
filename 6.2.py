n = int(input("Enter a number"))
def add_prime(n) :
   sum = 0
   c = 0
   for i in range(1,n+1) :
       if  i==2 or i==3 :
           sum  = sum + i
    
       elif i%2 == 0 or i%3==0 or i==1 :
              sum = sum

       else :
            sum = sum + i
        
   return(sum)
print(add_prime(n))
