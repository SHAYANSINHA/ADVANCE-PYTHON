

class person2 :
    def __init__(self,name,surname,yob):
        self._name1 = name ## protected variable
        self.__surname1 =surname ## private variable
        self.yob1 = yob ## public variable

sudh = person2 ("sudhanshu"," kumar",1990)
print(sudh._name1)
print(sudh._person2__surname1)
print(sudh.yob1)