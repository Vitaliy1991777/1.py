# import random as r
# a = {}
# k=0
# for i in range(1,6):
#         a[f'{i}'] = r.randint(-5000,5000)
# # print(a)
# # b = a.keys()
# # print(b)
# for i in a.values():
#         k+=abs(i)
#         if i > 3000:
#                 print(i, "more")
#         elif i < 0:
#                 print(i, "- no pay")

class Cirle():
        def __init__(self,r):
                self.R = int(r)
        def S(self):
                print("S",self.R)
        def P(self):
                print("P",self.R)
print(Cirle(20).S())
print(Cirle(120).P())
print(Cirle(250).S())
