a=input("Write a number")
lis=[]
count=0
if a.isdigit():
        for element in a:
            lis.append(element)
        t=0
        for i in range(0,len(lis)):
            n=int(lis[i])
            t=(n**len(a))+t
        b=int(a)
        for i in range(0,len(lis)):
            n=int(lis[i])
            if n==0:
                count=count+1
        if count!=len(lis):
            if (t==b):
                print("It is an armstrong number")
            else:
                print("It is not an armstrong number")
        else:
            print("It is not an armstrong number")
    
else:
    print("It is not a valid number")


