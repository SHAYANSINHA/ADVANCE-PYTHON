class Person :
    def __init__(shayan,name,surname,email_id,year_of_birth):
        shayan.name1 = name
        shayan.surname = surname
        shayan.email_id = email_id
        shayan.year_of_birth = year_of_birth
anuj_var = Person("anuj","bhandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu","kumar","sudhanshu@gmail.com",1990)
gargi = Person("gargi","kumari","gargi1996@gmail.com",1996)
print(anuj_var.name1)
print(anuj_var.surname)
print(anuj_var.email_id)
print(anuj_var.year_of_birth)
print(sudh.name1)
print(gargi.email_id)
print(type(sudh))