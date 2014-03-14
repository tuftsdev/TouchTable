
class SuperClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class SubClass(SuperClass):
    def __init__(self, a, b, c):
        super(SubClass,self).__init__(a,b)
        self.c = c


test = SubClass(5, 6, 7)
print test.c
print test.b
print test.a
