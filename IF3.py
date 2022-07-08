n1=int(input('1°:'))
n2=int(input('2°:'))
n3=int(input('3°:'))
if n1 > n2:
    n1,n2 = n2,n1
if n1 > n3:
    n1, n3= n3, n1
if n2 > n3:
    n2, n3 = n3, n2
print(n1,n2,n3)
print(n3,n2,n1)