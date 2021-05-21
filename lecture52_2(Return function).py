def login():
     usernameInput = input("Username : ")
     passwordInput = input("Password : ")
     if usernameInput == "admin" and passwordInput == "1234":
          return True
     else:
          return False
def showMenu():
     print("----- iShop -----")
     print("1. Vat Calculator")
     print("2. Price Calculator")
def Selectmenu():
     userSelected = int(input(">>"))
     return userSelected
def vatcal(totalPrice):
     vat = 7
     result = totalPrice + (totalPrice * vat / 100)
     return result
def pricecal():
     price1 = int(input("First Product Price : "))
     price2 = int(input("Second Product Price : "))
     return vatcal(price1 + price2)

print(pricecal())
