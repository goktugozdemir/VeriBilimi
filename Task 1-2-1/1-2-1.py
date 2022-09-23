def PrimeFun(n):
    a=3
    say=int(n/2)
    if (n < 2):
        return False
    elif (n == 2):
        return True
    elif (n%2==0):
        return False
    while(a<say):
        if(n%a==0):
            return False
        a=a+2
    return True

print(PrimeFun(101))
