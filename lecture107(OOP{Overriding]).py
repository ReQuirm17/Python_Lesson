class Animal():
    def eat(self):
        print("Eating Eating!")
class Cat(Animal):
    def eat(self):
        print("Meow!")      #Overriding process

cat1=Cat()
cat1.eat()
Animal1=Animal()
Animal1.eat()