print('依米咖啡馆咖啡名称:')
name = ('','蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚')
for a,name in enumerate(name):
    if a == 0:
        print('',end = '')
    else:
        print('品名',a,':',name)
