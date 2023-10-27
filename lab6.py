#Group 1
#Louise Price
#Ana Arosemena
encoded_password = None
decoded_password = None
password = None

def encode(password):
    global encoded_password
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password


def decode(encoded_password):
    global decoded_password
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit

    return decoded_password




#variable
selection= ""

while selection!="3":
    print("\nMenu")
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


    selection=input("\nPlease enter an option:")

    if selection=="1":
        password = input("Please enter your password to encode:")
        encode(password)
        print(f"Your password has been encoded and stored")
    elif selection == "2":
        decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.cd")
    else:
        pass



























































