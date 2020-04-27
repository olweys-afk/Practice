def load_data(filename):
    print("NOT Working")

def save_data(filename):
    print("NOT WORKING")

employees = {"Lenard":1234, "Kaye":2345}

text=""

while text != "q":

    print("\n Employee Directory \n")

    print("Enter 'f' to find, 'a' to add, 'd' to delete,'l' to load, 's' to save, 'q' to quit")
    text = input("Enter Option:")

    if text == "f":
        name = input("Enter Name:")
        if name in employees:
            print("Employee Local Number is:", employees[name])
        else:
            print("Not Found")

    elif text == "a":
        name = input("Enter name:")
        local = int(input("Enter Number:"))
        employees[name] = local

    elif text == "d":
        name = input("Enter Name:")
        sure = input("Are you sure you want delete" " "+ name +" "  "Yes or no:")
        if sure == "Yes":
            del employees[name]
            print("Employee has been deleted")
        else:
            print("Not Found")

    elif text == 'l':
        file_name = input("Enter FileName:")
        load_data(file_name)

    elif text == "s":
        file_name = input("Enter FileName:")
        save_data(file_name)





