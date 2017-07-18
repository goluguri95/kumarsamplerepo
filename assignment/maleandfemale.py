class Person:
    def __init__(self):
            pass
class male(Person):
    def __init__(self):
        pass
    def getGender(self):
        return "male"
class female(Person):
    def __init__(self):
        pass
    def getGender(self):
        return "female"
a = male()
print a.getGender()
b = female()
print b.getGender()
