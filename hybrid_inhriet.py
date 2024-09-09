class A:
    def display(self):
        print('dispaly from class A')
class B(A):
    def display(self):
        print('dispaly from class B')
class C:
    def display(self):
        print('dispaly from class C')
class D(B,C):
    def display(self):
        print("dispaly from class D")

d1 = D()
d1.display()
print(D.mro())