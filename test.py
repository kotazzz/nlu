from NewLifeUtils.CustomShellModule import *
from NewLifeUtils.ExceptModule import *

try:
    class A(object):
        def __init__(self):
            self.foo(0)
        def foo(self, zero):
            zero/zero
    def n():
        A()
    n()
except Exception as e:
    except_print("err")
shell = Shell()
shell.run()


