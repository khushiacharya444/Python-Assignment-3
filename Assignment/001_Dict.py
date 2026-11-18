#WAP to accept username and password from the user where the username and passwords are already stored in a dictionary format.
print("Secure Employee Account System")
accounts = {}
n = int(input("Enter number of accounts to create: "))

for i in range(n):
    print("\n Account", i+1)

    username = input("Enter username: ")

    while True:
        password = input("Enter password: ")
        has_upper = False
        has_lower = False
        has_number = False
        has_special = False
        has_space = False

        for ch in password:
            if ch.isupper():
                has_upper = True

            elif ch.islower():
                has_lower = True

            elif ch.isdigit():
                has_number = True

            elif ch.isspace():
                has_special = True

            else:
                has_special = True

        if (len(password) >= 8 and has_upper and has_lower and has_number and has_special and not has_space):
            confirm = input("Confirm password: ")

            if password == confirm:
                accounts[username] = password
                print("Account created successfully!")
                break
            else:
                print("Passwords do not match!")
                print("Please enter the confirm password again.")
        else:
            print("Password rejected!")

            if len(password) < 8:
                print("Password must contain at least 8 characters!")

            if not has_upper:
                print("Password must contain an uppercase alphabet.")

            if not has_lower:
                print("Password must contain an lowercase alphabet.")

            if not has_number:
                print("Password must contain a digit.")

            if not has_special:
                print("Password must contain a special character.")

            if has_space:
                print("Password must not contain any space.")

                print("Please enter the password again.")

print("\nStored Accounts:")
print(accounts)

print("\n Employee Login")
for i in range(5):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")

        if i < 4:
            print("Attempts remaining:", 4-i)
else:
    print("Access Denied!")
    print("Maximum login attempts reached!")