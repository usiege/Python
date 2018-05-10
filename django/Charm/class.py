
class PyClass:

    def f(self):
        print("This is a python class!")

    a = 0
    b = 0

    def g(runoob):
        print("This is a python class without self but runoob!")

    c = "111"
    d = "222"

    __private_a = 123

    # def __str__(self):
    #     return "%d, %d" % (self.a, self.b)
    #
    def __repr__(self):
        return "%s %s 0x%x" % (self.c, self.d, id(self))


p = PyClass()
print(p)
