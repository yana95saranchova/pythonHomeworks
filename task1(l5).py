from random import randint

l = []
i = 1
m = 10
while i <= m:
    l.append(randint(1, 1000000)) #не знаю насколько это все-таки  случайное число, границы же заданы(поэтому не знаю правильно ли поняла задание)
    i += 1
print(l)

print('Max element in list is',max(l))
