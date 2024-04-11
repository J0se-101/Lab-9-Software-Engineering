#Jose Pulido
def encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password

#Thomas Neubert

def decoder(password):
    decoded_password = ""
    for digit in password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit

    return decoded_password

current = ""

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit\n")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encoder(password)
        print("Your password has been encoded and stored!\n")
        current = encoded_password

    elif choice == "2":
        decoded_password = decoder(current)
        print("The encoded password is " + current + ", and the original password is " + decoded_password + "\n")

    elif choice == "3":
        break

