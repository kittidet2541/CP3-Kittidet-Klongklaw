class Customer():
    name=""
    lastname=""
    age=0
    def addCart(self):
        print("added to"+" "+self.name+" "+self.lastname+"'s cart")

customer1=Customer()
customer1.name="kittidet"
customer1.lastname="klongklaw"
customer1.age=22
customer1.addCart()