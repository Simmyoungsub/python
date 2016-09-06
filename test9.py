from numpy import outer

def gg(*args):
    return args[0],args[1]

def nn(a,b,c):
    return a
class A:
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def __init__(self,name="park",id="n",take="Y",out="N"):
        self.name = name
        self.id = id
        self.take = take
        self.out = out
        
    
    
a = A("jase")
b = A("park","N")
print a.getName()
print b.getName()   
print a.getId()
print b.getId()
