m, n, k = map(int, input().split())

c = m * n
if c >= k:
    print("Можно отломить")

else:
    print("не пролезет")