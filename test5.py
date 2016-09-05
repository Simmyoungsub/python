import os

import jpype


jpype.startJVM(jpype.getDefaultJVMPath(),"-ea","-Djava.class.path=c:/Java")

A = jpype.JClass("C")
c = A()

c.a()

jpype.shutdownJVM()
