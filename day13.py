n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

print()
n=5
for i in range(1,n+1):
    print((n-i)*" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

c=1
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()

print()
c=1
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+c),end=" ")
        c+=1
    print()