from random import randint

l1 = []
l2 = []
i = 0
len_l = 10
while i <= len_l:
    l1.append(randint(1, 10))
    l2.append(randint(1, 10))
    i += 1

print(l1)
print(l2)

l1.sort()
l2.sort()
list3=list(set(l1).intersection(set(l2)))
print(list3)