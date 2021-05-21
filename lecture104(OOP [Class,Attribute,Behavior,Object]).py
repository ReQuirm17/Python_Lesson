class Customer:         #Class
    name = ""           #Attribute
    lastname = ""       #Attribute
    age = 0             #Attribute

    def addCart(self):  #Behavior
        print("Added to Product to",self.name, self.lastname, "cart")

customer1 = Customer()  #Object

customer1.name = input('>>')
customer1.lastname = "Chullapamorn"
customer1.addCart()

customer2 = Customer()
customer2.name = "Haritch"
customer2.lastname = "Utchavanich"
customer2.addCart()

customer3 = Customer()
customer3.name = "Phuvis"
customer3.lastname = "kerdpramote"
customer3.addCart()

customer4 = Customer()
customer4.name = "Phudit"
customer4.lastname = "Kittisomprayoonkool"
customer4.addCart()