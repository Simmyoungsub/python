def sum(a,b):
    return a+b
def sub(a,b):
    return a-b

a = 0

def A(a):
    def B():
        global a
        print a
    B()
    
x=4

ob = object()

class X(object):
    x = x+1
    y = x
    z = x
    
    def method(self):
        print(self.x)
        print(x)
        print(self.y)
        
inst = X()
inst.method()

b = X()
print b.__class__.__base__
