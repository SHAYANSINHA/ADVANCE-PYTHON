class person :

    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id ):
        print("take and mail id form a person and print it : " , email_id)

    def ask_name(self):
        name=input("tell me your name : ")
        return name

    def ask_dob(self):
        dob = input ("tell me your date_of_birth : ")
        return dob

sudh = person()
anuj = person()
gargi = person()
krish = person()
hitesh = person()

sudh.email_id_input("sudhanshu@gmail.com")

krish.email_id_input("krish@gmail.com")

print(" age of sudh is : " ,sudh.age(2023,1990))

print(sudh.ask_name())

print(sudh.ask_dob())