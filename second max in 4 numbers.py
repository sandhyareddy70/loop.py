# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# if a>b:
#     max1=a
# else:
#     max1=b
# if c>d:
#     max2=c
# else:
#     max2=d
# if max1>max2:
#     print(max2," is second max")
# else:print(max1,"is second max")
        

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
if a>b:
    max1=a
    smax1=b
else:
    max1=b
    smax1=a
if c>d:
    max2=c
    smax2=d
else:
    max2=d
    smax2=c
if max1>max2:
    if max2>smax1:
        print(max2," is second max")
    else:
        print(smax1,"is second max")
elif max1>smax2:
    print(max1," is a second max")
else:
    print(smax2," is second max")
    
        




