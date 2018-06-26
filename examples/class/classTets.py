class Spam:
    def __init__(self,ham,egg):
        self.ham = ham
        self.egg = egg
    def output(self):
        sum = self.ham + self.egg
        print("{0}".format(sum))

    def func0(self):
        self.a=10

    def func1(self):
        print(self.a)

spam = Spam(5,10)
spam.output()
spam.func0()
spam.func1()

'''
class A:
    def method(self):
        print("class A")

class B:
    def method(self):
        print("class B")

class C(A):
    def method(self):
        print("class C")

class D(B,C):
    pass

d = D()
d.method()


class Spam:
    __attr = 100  ##private
    def __init__(self):
        self.__attr = 999
    def method(self):
        self.__method()
    def __method(self):
        print(self.__attr)

spam =Spam()
spam.method()   #OK
spam.__method() #NG
spam.__attr     #NG

'''
