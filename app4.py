import random

x = random.randint(1, 11)

while x == 3:
    print("Well done !")
    if x != 3:
        print("Keep trying")
    else:
        print("Wrong")
        break
