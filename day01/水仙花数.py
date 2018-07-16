#number = a**3+b**3+c**3
#a = number//100 c=number% b=number//10%10
n = 100
while  n<1000:
    if n == (n//100)**3+(n//10%10)**3+(n%10)**3:
        print(n)
    n+=1
