import math
n,m=1,50
a1,b = 3,5
d=(a1*b)//math.gcd(a1,b)
a=(n+d)-(n%d)
l=m-m%d
no=((l-a)//d)+1
print((no*(a+l))//2)
