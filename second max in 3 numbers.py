# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a != b and a != c and b != c:
#     if a>b:
#         if a>c:
#             if c>b:
#                 print(c, "is the second max")
#             else:
#                 print(a, "is the second max")
#         else:
#             print(a, "is the second max")
#     elif b>c:
#         if c>a:
#             print(b, "is the second max")
#         else:
#             print(c, "is the second max")
# else:
#     print("Input numbers are not distinct. Please enter three distinct numbers.")

    
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b:
    max=a
    smax=b
else:
    max=b
    smax=a
if c>max:
    if c>smax:
        print(max)
    else:
        print(smax)
if c<max:
    if c<smax:
        print(smax)
    else:
        print(c)
        





