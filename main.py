def menu():
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")
def encode(password):
    encoded_password = " "
    for digit in password:
        encode_digits = str((int(digit)+ 3) % 10)
        encoded_password = encode_digits
    return encoded_password


def main():
    while True:
        print()
        menu()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your encoded password is:", encoded_password)

        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


