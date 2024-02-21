fruitList = ["banana", "orange", "apple"]

# Create a string of lowercase fruits separated by commas
fruit_list_string = ", ".join([x.lower() for x in fruitList])

print("You can enter your fruits from this list: " + fruit_list_string)

fruit = input("Enter your fruit: ").lower()
color = input("Enter its color: ").lower()

if fruit in fruitList:
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Color not recognized")
else:
    print("Fruit not recognized")
