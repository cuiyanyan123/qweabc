a = int(input('请输入您的身高'))
b = int(input('请输入您的身价'))
c = int(input('请输入您的颜值分'))
if a>180 and b>1000000 and c>99:
    print('高富帅')
elif b>1000000 and c>99:
    print('富帅')
elif c>99:
    print('帅')
elif a<160 and b<100 and c<60:
    print('矮穷锉')
else:
    print('少年加油吧,争取成为高富帅')
