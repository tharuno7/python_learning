#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# n = int(input("enter num:").strip())
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and 2<=n<=5:
#     print("Not Weird")
# elif 6<=n<=20:
#     print("Weird")
# else:
#     print("Not Weird")

#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    leap = False
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    

year = int(input("enter year:"))
print(is_leap(year))