

from utils.utils1 import person2
obj = person2("sudhanshu","kumar",8988)

print(obj._name1)
print(obj._person2__surname1)
print(obj.yob1)

class person1 :
    def __init__(self,name,surname,yob):
        self._name1 = name ## protected variable
        self.__surname1 =surname ## private variable
        self.yob1 = yob ## public variable

sudh = person1 ("sudhanshu"," kumar",1990)
print(sudh._name1)
print(sudh._person1__surname1)
print(sudh.yob1)