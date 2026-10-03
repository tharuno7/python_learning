# #FOR LOOP PROBLEMS
# #basic understanding
# #1. print numbers from 1 to 10 in one line
# for i in range(1,10+1):
#     print(i,end=" ")
# print()
# #2. print even numbers from 5 to 30 in one line
# for i in range(5,30+1):
#     if i%2==0:
#         print(i,end=" ")
# print()
# #3. print odd numbers from 5 to 30 in one line
# for i in range(5,30+1):
#     if i%2!=0:
#         print(i,end=" ")
# print()
# #4. print numbers divisible by 5 from 1 to 30 in one line
# for i in range(1,30+1):
#     if i%5==0:
#         print(i,end=" ")
# print()
# #5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
# for i in range(1,100+1):
#     if i%5==0 and i%7==0:
#         print(i,end=" ")
# print()
# #6. sum of numbers from 10 to 25 
# sum=0
# for i in range(10,26):
#     sum+=i
# print(sum)
# print()
#7. sum of numbers in any list
# n=list(map(int,input("enter list:").split()))
# sum=0
# for i in n:
#     sum+=i
# print(sum)

#8. multiplication table of a number 
# n=int(input("table to n:"))
# for i in range(1,n+1):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#interview problems
#9. factorial 
# n=int(input("factorial of num:"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)
#10. fibonacci 
# n=int(input("enter n times:"))
# a,b=map(int,input("enter nums:").split())
# for i in range(n+1):
#     print(a,end=" ")
#     a,b=b,a+b


#11. reverse a string
# n=input("enter name:")
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end=" ")
#12. count vowels in a string
# n=input("enter string:")
# count=0
# for ch in n:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)


#13. count z's and y's in a string
# n=input("enter string:")
# count=0
# for ch in n:
#     if ch in "zZyY":
#         count+=1
# print(count)
#14. check whether a number is prime number or not 
# n=int(input("enter num:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("it is prime")
# else:
#     print("not prime:")



#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
# n=11
# i=1
# while i<n:
#     print(i)
#     i+=1
# print()
# #print even numbers from 1 to 10
# n=10
# i=0
# while i<n:
#     if i%2==0:
#         print(i)
#     i+=1
#print numbers divisible by both 5 and 7 from 1 to 500 
# n=500
# i=1
# while i<n:
#     if i%5==0 and i%7==0:
#         print(i,end=" ")  #35 70 105 140 175 210 245 280 315 350 385 420 455 490 
#     i+=1
#interview problems
#count digits
# n=int(input("enter num:"))
# count=0
# for i in str(n):
#     count+=1
# print(count)
# print()
# # in while loop
# n= int(input("enter num:"))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print("count of digit:",count)
# print()
# #count digit in string
# n=input("enter string:")
# count=0
# for i in n:
#     if i>='0' and i<='9':
#         count+=1
# print(count)

#reverse a number
# n=int(input("enter num:"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)
# palindrome number 
# n=int(input("enter num:"))
# original=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if original==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# #palindrome string (without slicing, built in function)
# n=input("enter string:")
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end=" ")

#armstrong number
n=int(input("enter num:"))
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**count
    temp//=10

if sum==n:
    print("armstrong num")
else:
    print("not armstrong num")