list1 = list(range(1, 101))
print(list1)
new_list = []
i = 0
while i < len(list1):
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        new_list.append(list1[i])
    i += 1

print(new_list)
