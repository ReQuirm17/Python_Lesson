try:
    input1=int(input("A: "))
    input2=int(input("B: "))
    print(input1/input2)
except ValueError:
    input2=0
    print("Error: ! Re-enter Number")
except ZeroDivisionError:
    print("Error: !You can't Enter 0")
except:
    print("Error!")