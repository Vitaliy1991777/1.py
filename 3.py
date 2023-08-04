a, b, l, N = map(int, input().split())



while N != 0:
    N = N * 2
    b = b * (N-2)
    a = a + (a * (N-2))
    l = l * 2
    break
print(a + b + l)

