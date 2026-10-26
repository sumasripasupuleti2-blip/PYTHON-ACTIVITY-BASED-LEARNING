balance = float(input("Enter initial account balance (Rs.): "))
number_of_transactions = int(input("Enter number of transactions: "))

total_deposits = 0
total_withdrawals = 0
valid_transactions = 0
invalid_transactions = 0

if balance < 0 or number_of_transactions < 0:
    print("Invalid initial balance or transaction count.")

else:
    for i in range(number_of_transactions):
        print("\nTransaction", i + 1)

        transaction_type = input("Enter D for Deposit or W for Withdrawal: ")
        transaction_type = transaction_type.upper()

        amount = float(input("Enter transaction amount (Rs.): "))

        if amount <= 0:
            print("Invalid amount. Amount must be greater than zero.")
            invalid_transactions = invalid_transactions + 1

        elif transaction_type == "D":
            balance = balance + amount
            total_deposits = total_deposits + amount
            valid_transactions = valid_transactions + 1
            print("Deposit successful.")

        elif transaction_type == "W":
            if amount > 10000:
                print("Withdrawal limit exceeded.")
                invalid_transactions = invalid_transactions + 1

            elif amount > balance:
                print("Insufficient balance.")
                invalid_transactions = invalid_transactions + 1

            else:
                balance = balance - amount
                total_withdrawals = total_withdrawals + amount
                valid_transactions = valid_transactions + 1
                print("Withdrawal successful.")

        else:
            print("Invalid transaction type.")
            invalid_transactions = invalid_transactions + 1

    print("\n--- ATM TRANSACTION SUMMARY ---")
    print("Final account balance: Rs.", round(balance, 2))
    print("Total deposits: Rs.", round(total_deposits, 2))
    print("Total withdrawals: Rs.", round(total_withdrawals, 2))
    print("Valid transactions:", valid_transactions)
    print("Invalid transactions:", invalid_transactions)
