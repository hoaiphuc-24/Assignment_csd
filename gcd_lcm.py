def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a,b):
    return (a*b)/gcd(a,b)
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("GCD of",a,"and",b,"is",gcd(a,b))
#print("LCM of",a, "and",b,"is", lcm(a,b))
#end
def isPrime():
    n = int(input("Nhap n:"))
    if n<2:
        print("Nhap sai")
    else:
        for i in range(2,(n//2)+1):
            if i%2==0:
                print("{} is not Prime".format(n))
                break
        else:
            print({n},"is Prime")

#isPrime()
#end

def primenumbers(m,n):
    if m<0 or n<0:
        print("Nhap sai")
    elif m>=n:
        print("So thu nhat lon hon so thu hai")
    else:
        for value in range (m,n+1):
            if value<2:
                continue
            for i in range(2,(value//2)+1):
                if value%i==0:
                    break
            else:
                print(value,end='\n')
#m=int(input("Nhap m: "))
#n=int(input("Nhap n: "))
#primenumbers(m,n)
#end
def isPerfect(x=6):
    if x<=0:
        return False
    else:
        sum=0
        for i in range(1,x):
            if sum%i==0:
                    sum+=i
    if sum==x:
        print(x,"is a perfect number")
    else:
        print(x,"is not a perfect number")
#num=int(input("Nhap so:"))
#isPerfect(num)









