def fact(a):
    if isinstance(a,float):
        print('factorial is possible for only integers')
    elif a<0:
        print('factorial is not possible for negetive integers')
    elif a==0:
        return 1
    else:
        return a*fact(a-1)
print('the factorial of 10.1 is',fact(10.1))
print('the factorial of -64 is ',fact(-64))
print('the factorial of 10 is ',fact(10))
