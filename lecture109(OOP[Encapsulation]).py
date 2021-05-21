class Animal():
    def eat(self):
        print("Eating Eating!")
class Cat(Animal):
    __name = ""                 #Encap
    def setName(self,text):     #setter function
        self.name = text
        print("Setting New Name = ",self.name)

    def eat(self):
        print("Meow!",self.name)      #Overriding process

cat1=Cat()
cat1.__name = "TT"
cat1.eat()
#เกิด Error เพราะ setterFunction ถูก Encap ไว้
#--------ถ้าจะให้ถูก---------
cat1 = Cat()
cat1.setName("TT")
cat1.eat()



