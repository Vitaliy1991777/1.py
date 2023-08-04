a, b, c, x, y = map(float, input().split())

# while a != 0 and b != 0 and c != 0 and x != 0 and y != 0:
if a <= x and b <= y or b <= x and a <= y:
        print("пролезет")
elif c <= x and a <= y or a <= x and c <= y:
        print("пролезет")
elif b <= x and c <= y or c <= x and b <= y:
        print("пролезет")
else:
    print("не пролезет")