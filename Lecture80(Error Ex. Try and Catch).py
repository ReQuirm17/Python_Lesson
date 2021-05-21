import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try: #Try
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except: #catch
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next ecntry.")
        print()
print("The reciprocal of", entry, "is", r)