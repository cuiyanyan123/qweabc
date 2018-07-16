a = int(input('请您输入一个年份'))
if (a%4==0 and a%100!=0) or a%400==0:
    print('这个年份是闰年')
else:
    print('这个年份是平年')
