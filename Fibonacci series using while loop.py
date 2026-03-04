num=int(input("Enter a num:"))
a=0
b=1
c=0
while c<num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    c+=1