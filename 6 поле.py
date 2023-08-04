p = 100
u = 20
s = 0

g1 = 0
g2 = 0
g3 = 0

while p < 120:
        p = p * 1.05
        g1 += 1
        print(g1)
        if u < 22:
            u = u * 1.02
        g2 += 1
        print(g2)
        if s < 800:
            s = p * u
        g3 += 1
        print(g3)

p = 100
u = 20
s = 0
g3 = 0
while s < 800:

        s = p * u
        g3 += 1
        print(g3)