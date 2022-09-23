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


def HunPrime():
    n=3
    list=[2]
    for c in range (1000):
     if(len(list)>99):
         break
     if(PrimeFun(n)==True):
         list.append(n)
         n=n+2
     else:
         n=n+2
    print(list)


HunPrime()