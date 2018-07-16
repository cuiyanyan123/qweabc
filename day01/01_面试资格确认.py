age =int(input('请输入你的年龄：'))
subject =input('请输入你的专业:')
college =input('是否是重点大学:')
if age > 25 and subject == '电子工程专业':
    print('面试成功')
elif college == '是' and subject == '电子信息工程专业':
    print('面试成功')
elif age < 28 and subject == '计算机':
    print('面试成功')
else:
    print('不符合面试要求')
