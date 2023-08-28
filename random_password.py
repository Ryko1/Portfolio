
import random
import time


# Method 1
def random_password():
    char = "abcedfghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password_len = 16

    for x in range(0, password_len):
        x = random.choice(char)
        print(x, end='')


limit = 0
while limit != 3:
    input("\nPress enter to generate a random password: ")
    random_password()
    limit += 1

print("\n\n\nMethod 2")


# Method 2
def random_password2():
    char = "abcedfghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password_len = 16
    password = ""

    for x in range(0, password_len):
        x = random.choice(char)
        password += x

    print(password)


limit2 = 0
while limit2 != 3:
    input("Press enter to generate a random password: ")
    random_password2()
    limit2 += 1


print("\n\n\nMethod 3(Bonus)")


# Method 3 (Bonus/Challenge)
def loading_password():
    char = "abcedfghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password_len = 16
    # --creates a randomized list of 16 characters from the list 'char'
    # --Must Do First!
    password_val = [random.choice(char) for x in range(0, password_len)]

    for progress in range(0, password_len, 1):
        # --'.join' can be used to combine all the characters in the list
        # --must include a 'seperator'("") before the statement
        loading_pass = "".join(password_val[:progress])
        loading_str = "Generating password..."
        loading_display = loading_str + loading_pass
        print(loading_display, end='\r')
        time.sleep(0.2)

    print(f"Password is: {loading_pass}")


input("Press enter to generate a random password: ")
loading_password()
