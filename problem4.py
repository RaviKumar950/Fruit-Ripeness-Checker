print("You can Enter your Fruits of this list","Banana\t","Orange\t","Apple\t")
fruits = input("Enter Your Fruits:>\t").lower()
lower_input = fruits.lower()
print("You can Enter your color of this list: Green\tYellow\tBrown")
color = input("Enter Your color:>\t").lower() 


if fruits == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")
    else:
        print("Color Not Recognize")
elif fruits == "orange":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")
    else:
        print("Color Not Recognize")
elif fruits == "apple":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("OverRipe")
    else:
        print("Color Not Recognize")

else:
    print("Fruits Not Recognize")

