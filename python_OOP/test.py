class Cat:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s爱吃鱼" % self.name)
    def drink(self):
        print("%s爱喝水" %self.name)
    

tom = Cat("tom")
tom.eat()
tom.drink() 
print(tom.name)
addr = id(tom)
print("%x" %addr)