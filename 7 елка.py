# n = int(input())
# s=""
# for i in range(1, n+1):
#
#         s = s + '*'
#         print(s)

##########################################

# n = int(input())
# a = "*"
# for i in range(n, -1, -1):
#
#
#     print(' ' * (n - i), a * n)

###########################################

# n = int(input())
#
# for i in range(n, -1, -1):
#     for j in range(1, i + 1):
#         print(j, sep='', end='')
#     print()

###########################################

n = int(input())
a = "*"
a = a.center(1,' ')
for i in range(n, -1, -1):


    print(' ' * (n-i) + a * i)

