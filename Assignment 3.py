def factorial(n):
    if n == 1:
       return n
    elif n < 1:
        
        if n==0:
           print("The factorial of 0 is equal to: 1")
        else:
            return ("It is not a Valid Number")
    else:
       return n*factorial(n-1)
a=input("Enter a number: ")
if a.isdigit():
    if int(a)!=0:
        print("The factorial of",a," is equal to:",factorial(int(a)))
    else:
        factorial(int(a))
else:
    print("It is not a valid number.")

                
        
    

