class Person :
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname


    def __init__(self, name,  year_of_birth):
        self.name = name

        self.year_of_birth = year_of_birth
    def age(self,current_year):
         return current_year - self.year_of_birth

anuj_var = Person("anuj",1994)
sudh = Person("sudhanshu",1990)
gargi = Person("gargi",1996)
print(sudh.age(2023))