#def raise_to_power(num,pow_num):
    #res=1
    #for index in range(pow_num):
     #   res=res*num
    #return res

#print(raise_to_power(5,2))

n = int(input("enter the base number : "))
m = int(input("enter the power number  : "))

def add(a, b):
    num = a
    for i in range(b):
        num += 1
    return num

def multiply(a, b):
    num = 0
    for i in range(b):
        num = add(num, a)
    return num

def exponent(a, b):
    num = 1
    for i in range(b):
        num = multiply(num, a)
    return num

print(exponent(n, m))


