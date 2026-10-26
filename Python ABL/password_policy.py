password = input("Enter a sample password to check: ")

failed_rules = 0

uppercase_found = False
lowercase_found = False
digit_found = False
special_found = False

print("\n--- PASSWORD POLICY VALIDATION ---")

if len(password) < 8:
    print("Failed: Password must contain at least 8 characters.")
    failed_rules = failed_rules + 1

for character in password:
    if character.isupper():
        uppercase_found = True

    if character.islower():
        lowercase_found = True

    if character.isdigit():
        digit_found = True

    if character in "!@#$%^&*()-_+=?":
        special_found = True

if uppercase_found == False:
    print("Failed: At least one uppercase letter is required.")
    failed_rules = failed_rules + 1

if lowercase_found == False:
    print("Failed: At least one lowercase letter is required.")
    failed_rules = failed_rules + 1

if digit_found == False:
    print("Failed: At least one digit is required.")
    failed_rules = failed_rules + 1

if special_found == False:
    print("Failed: At least one special character is required.")
    failed_rules = failed_rules + 1

repeated_found = False

for i in range(len(password) - 2):
    if password[i] == password[i + 1] and password[i] == password[i + 2]:
        repeated_found = True

if repeated_found == True:
    print("Failed: Three consecutive identical characters are not allowed.")
    failed_rules = failed_rules + 1

if "password" in password.lower():
    print("Failed: The word 'password' is not allowed.")
    failed_rules = failed_rules + 1

if failed_rules == 0:
    print("Password satisfies all the defined policy rules.")
else:
    print("Total failed rules:", failed_rules)

print("Validation completed.")
