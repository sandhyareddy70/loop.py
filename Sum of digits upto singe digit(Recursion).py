def num(n):
    if n>0 and n<=9:
        return n
    else:
        s=0
        while n>0:
            r=n%10
            s=s+r
            n=n//10
        return num(s)
n=int(input("Enter a number:"))
print(num(n))