import time


def calculator():
    print("Welcome to the Calculator! ")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    op = input("please enter an operator: ")
    result = 0

    if op == "+":
        result = num1 + num2
        print(result)
    elif op == "-":
        result = num1 - num2
        print(result)
    elif op == "/":
        result = num1 / num2
        print(result)
    elif op == "*":
        result = num1 * num2
        print(result)
    else:
        calculator()


def unit_converter():
    units = ["Kb", "Mb", "Gb", "Tb"]
    print("Welcome to the Memory Unit Converter")
    print(units)
    first_unit = input("What unit would you like to convert?: ")
    second_unit = input("What would you like to convert it to?: ")
    first_unit_amount = int(input("Enter amount: "))


    if first_unit == "Kb" or "kb" and second_unit == "Mb" or "mb":
        result = (first_unit_amount / 1000)
        print(str(first_unit_amount) + " Kilobytes is equal to " + str(result) + " Megabytes")
        time.sleep(3)
    elif first_unit == "Kb" or "kb" and second_unit == "Gb" or "gb":
        result = (first_unit_amount / 1000000)
        print(str(first_unit_amount) + " Kilobytes is equal to " + str(result) + " Gigabytes")
        time.sleep(3)
    elif first_unit == "Kb" or "kb" and second_unit == "Tb" or "tb":
        result = (first_unit_amount / 1000000000)
        print(str(first_unit_amount) + " Kilobytes is equal to " + str(result) + " Terabytes")
        time.sleep(3)

    elif first_unit == "MB" or "mb" and second_unit == "Kb" or "KB":
        result = (first_unit_amount * 1000)
        print(str(first_unit_amount) + " Megabytes is equal to " + str(result) + " Kilobytes")
        time.sleep(3)

# def unit_convertor():
#     print("Welcome to the unit converter!")
#     print("")
#     print("Kb, Mb, Gb, Tb")
#     print("")
#     unit = input("Enter the unit you wish to convert: ")
#     unit2 = input("What do you want to convert it to? ")
#     if unit == "Kb" and unit2 == "Mb":
#         kb1 = input("Please input the amount of kilobytes you want to convert")
#         kb1 = int(kb1)
#         kb2 = (kb1 / 1024)
#         kb3 = str(kb2)
#         print(kb3 + "GB")
#
#     while True:
#         mb1 = input("Please input the amount of megabytes you want to convert")
#         mb1 = int(mb1)
#         mb2 = (mb1 / 1024)
#         mb2 = str(mb2)
#         print(mb2 + " GB")

def main_function():
    print("")
    print("Welcome to my multi-use tool.")
    print("")
    option = (input("Which program would you like to use?\n"
                   "Press 1 for Calculator\n"
                   "Press 2 for Data units converter: "
                   " "
                       ))
    if option == "1":
        print("")
        calculator()
    elif option == "2":
        print("")
        unit_converter()
    else:
        print("")
        main_function()



def password_function():
    password = "Password"
    guess = ""
    guess_count = 0
    total_guesses = 3
    out_of_guesses = False

    while guess != password and not out_of_guesses:
        if guess_count < total_guesses:
            guess = input("Please enter password: ")
            guess_count += 1
            if guess_count == 1:
                guess = input("Incorrect. Please re-enter password [1/3]: ")
                guess_count += 1
            if guess_count == 2:
                guess = input("Incorrect. Please re-enter password [2/3]: ")
                guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Password entered incorrectly too many times.")
    else:
        print("Password entered correctly.")
        main_function()


username = "Liam"
userGuess = ""
userGuessLimit = 3
userGuessCount = 0
noMoreGuesses = False

while userGuess != username and not noMoreGuesses:
    if userGuess == "x":
       main_function()

    elif userGuessCount < userGuessLimit:
        userGuess = input("Please enter username: ")
        userGuessCount += 1
    else:
        noMoreGuesses = True

if noMoreGuesses:
    print("Too many failed attempts.")
else:
    print("Username accepted")
    password_function()