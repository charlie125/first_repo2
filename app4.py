print("Sunny")
print("Cloudy")
print("forsty")
print("Warm")

weather = str(input("Please enter what types of weather:"))
degree = float(input("Please enter degree:"))

if weather.lower() == "forsty":
    if degree <= 10:
        print("It's forsty outside!")
    else:
        print("It's time for picnic.")
else:
    print("well, seem to having a nice weather.")
