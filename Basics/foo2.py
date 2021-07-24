# Suppose this is foo2.py.
import os, sys; sys.path.insert(0, os.path.dirname(__file__)) # needed for some interpreters

def functionA():
    print("a1")
    from foo2 import functionB
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")

print("t1")
if __name__ == "__main__":
    print("m1")
    functionA()
    print("m2")
print("t2")