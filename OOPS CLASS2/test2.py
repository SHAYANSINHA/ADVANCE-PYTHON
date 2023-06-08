import test1
print(test1)

obj3 = test1.person1("sudhanshu", " kumar", 1999)
print(obj3.yob1)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)

class person :

    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self , current_year):
        return current_year - self.yob

    def __age1(self , current_year):
        return current_year - self.yob

obj = person()
print(obj._age(2023))
print(obj._person__age1(2023))

class employee(person) : ## INHERITANCE
    _name = "SHAYAN"
    __surname = "SINHA ROY"
    yob = 1994
obj1=employee()
print(obj1._age(2023))
print(obj1._person__age1(2023))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)# private variable alwayas associated to the particular classes
print(obj1._employee__surname)