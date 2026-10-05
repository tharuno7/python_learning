n=5
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
print()
n=5
for i in range(n):
  print((n-i)*" " + i*'* ')

  
print()
n=4
for i in range(1,n+1):
  print(i*'*')

print()
n=5
for i in range(n):
  for j in range(n):
    if i==j or i+j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
print()
print()
print()
n=7
for i in range(n):
  for j in range(n):
    if j==i or j==n-i-1 or i==n//2 or j==n//2:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
print()

