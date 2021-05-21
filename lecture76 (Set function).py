userInput =int(input("Your favorite fruit: "))
myfruits =set()
while(len(myfruits)<userInput):
    myfruits.add(input("Fruits: "))
    print(myfruits)