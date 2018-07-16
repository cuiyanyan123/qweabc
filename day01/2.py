a = int(input('有一个数这样说三三之数剩二,五五之数剩三,七七之数剩二,请输入答案'))
if a%3==2 and a%5==3 and a%7==2:
    print(a)
else:
    print('答案错误')
