#玩家需要输入一个数字，电脑随机出一个数字，
import random
player = int(input('请输入一个数字：'))
computer = random.randint(1,10)
if player == computer:
    print('哇，好厉害！')
else:
    print('运气不咋地呀！')
