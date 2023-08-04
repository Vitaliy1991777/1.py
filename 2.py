a, b, c = map(int, input().split())

if a > b > c:

    print(a-c)
elif b > a > c:

    print(b - c)
elif c > a > b:

    print(c - b)
elif a > c > b:

    print(a - b)
elif b > c > a:

    print(b - a)
elif c > b > a:

    print(c - a)