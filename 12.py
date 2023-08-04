n = int(input('Коллличество вещей: '))
arr = {'Фонарь': 0.1, 'Палатка': 3, 'Чайник': 1, 'Вода': 2, 'Куртка': 0.8}

for _ in range(n):
    i = input("Введите название вещи: ")
    j = float(input("Введите вес: "))


#arr = sorted(arr, key=lambda x: -x[1])
items = sorted(arr.items(), key=lambda x: -x[1])
print(arr)

n = int(input("Введите общий вес: "))

d = {k:v for k, v in arr.items() if v <= n and (n := n - v) >= 0}
#d = {i: j for j in arr if j <= n and (n := n - j) >= 0}
print(d)




