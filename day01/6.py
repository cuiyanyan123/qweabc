a = 1.75
b = 80.5
BMI = b/(a*a)
print(BMI)
if BMI<18.5:
    print('过轻')
elif 18.5 <= BMI <= 25:
    print('正常')
elif 25 < BMI <= 28:
    print('过重')
elif 28 < BMI <= 32:
    print('肥胖')
else:
    print('严重肥胖')

