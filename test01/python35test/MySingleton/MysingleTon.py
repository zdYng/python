class My_singleton(object):
    _instance = None
    def __new__(cls,*args,**kw):
        if not cls._instance:
            cls._instance = super(My_singleton,cls).__new__(cls,*args,**kw)
        return cls._instance
class MyClass(My_singleton):
    a =1
one = MyClass()
two = MyClass()
if one ==two:
    print("True")
if one is two:
    print("True")
print(id(one))
print(id(two))