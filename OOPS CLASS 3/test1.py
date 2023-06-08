class car : # PARENT CLASS
    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre=tyre
    def mileage(self):
        print("mileage of this car ")
c = car("solid","v6","radial")
print(c)

class tata(car) :  # CHILD CLASS
    pass

t = tata("solid","v8","radial1")
print(t)
print(t.mileage())
