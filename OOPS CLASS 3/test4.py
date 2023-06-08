""" method overrridding MEANS IF IN A PAERENT CLASS AND IN A CHILD CLASS

 METHOD NAME ARE SAME BUT DIFFERENT DEFINATION, THEN IT GOING TO OVERRIDING FIRST ONE. """
class ineuron:
    def student(self):
        print("print the details of all the students")
    def achivers(self):
        print("print the list of all the achiver ")
    def hall_of_fame(self):
        print("print everyone form hall of fame ")

class ineuron_vision(ineuron):

    def student(self):
        print("these are the filters student list ")

iv =  ineuron_vision()
iv.student()