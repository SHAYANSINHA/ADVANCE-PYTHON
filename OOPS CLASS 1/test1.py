class Person :
    def __init__(self,name,surname,email_id,year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth
anuj_var = Person("anuj","bhandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu","kumar","sudhanshu@gmail.com",1990)
gargi = Person("gargi","kumari","gargi1996@gmail.com",1996)
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.email_id)
print(anuj_var.year_of_birth)
print(sudh.name)
print(gargi.email_id)
print(type(sudh))