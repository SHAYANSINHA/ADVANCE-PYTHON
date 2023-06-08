"""DATA encaptulations MEANS YOU ARE NOT ALLOW A USER TO MODIFY THE VALUE OF VARIABLE DIRECTLY,
 THEN YOU WILL BE ABLE TO HELP OF encaptulations"""

""" IN CASE OF PUBLIC VARIABLE I DIRECTLY MODIFY IT ON RUNTIME, BUT NOT IN CASE OF PRIVATE VARIABLE ."""

class ineuron:
    def __init__(self):
        self.students1 = "data science "

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "data analytics"
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "data science "

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1 = new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "big data"
i1.students()
i1.student_change("sudhanshu")
i1.students()