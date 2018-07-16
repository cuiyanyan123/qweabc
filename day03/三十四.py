a = input('请输入一行字符：')
#len(a)
num=0
for i in a: 
    if i.isdigit()==True:
        num+=1
print(num)
