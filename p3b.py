# Read multi-digit number as string
number = input("Enter a multi-digit number: ")

# Validate - only digits allowed
if not number.isdigit():
    print("Invalid input! Please enter digits only.")
else:
    print("\nNumber entered : {}".format(number))
    print("─" * 30)
    print("{:<10} {:<10}".format("Digit", "Frequency"))
    print("─" * 30)

    # Count frequency of each digit (0-9)
    found = False
    for digit in range(10):
        count = number.count(str(digit))
        if count > 0:
            print("{:<10} {:<10}".format(digit, count))
            found = True

    print("─" * 30)
    print("Total Digits   : {}".format(len(number)))
    print("Unique Digits  : {}".format(len(set(number))))
