def welcome_prompt():
    print("\n----------------------------------------")
    print("Welcome to the Password Generator")
    print("----------------------------------------\n")
     
def length_prompt():
    print("How long should the password be?")
    while True:
        try:
            password_length = int(input("").strip())
            if password_length < 8:
                print("Passwords Required a minimum of 8 characters.")
            if password_length == 0:
                print("Passwords can't be 0 Characters.")
        except  ValueError:
            print("Please Enter a Number.")
        else:
            return password_length            

def upper_prompt():
    print("Include uppercase letters? (y/n)")
    while True:
            upper = str(input("").strip().lower())
            first_letter = upper[0]
            if first_letter == "n":
                return False
            elif first_letter == "y":
                return True
            elif first_letter == "":
                print("Answer Yes or No")
            else:
                print("Answer Yes or No")

def symbols_prompt():
    print("Include symbols? (y/n)")
    while True:
            upper = str(input("").strip().lower())
            first_letter = upper[0]
            if first_letter == "n":
                return False
            elif first_letter == "y":
                return True
            elif first_letter == "":
                print("Answer Yes or No")
            else:
                print("Answer Yes or No")

def num_prompt():
    print("Include numbers? (y/n)")
    while True:
            upper = str(input("").strip().lower())
            first_letter = upper[0]
            if first_letter == "n":
                return False
            elif first_letter == "y":
                return True
            elif first_letter == "":
                print("Answer Yes or No")
            else:
                print("Answer Yes or No")

def word_prompt():
    print("Would you like a word based pass? (y/n)")
    while True:
            upper = str(input("").strip().lower())
            first_letter = upper[0]
            if first_letter == "n":
                return False
            elif first_letter == "y":
                return True
            elif first_letter == "":
                print("Answer Yes or No")
            else:
                print("Answer Yes or No")

