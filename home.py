"""TASK 1:
Program: Currency Input Program
Objective:
This program asks the user to enter a currency type and an amount.
It checks if the amount entered is a valid number.
Then it displays the currency and amount entered by the user.
"""
transactions = []
for i in range(4):  #task-3 as loop is said to be applied in the  same process as the task 1 and 2 

    # Ask the user to enter the currency type
    currency = input("Enter currency (USD or EUR or JPY or GBP): ")

    # Ask the user to enter the amount
    amount = float(input("Enter amount: "))
    print("Currency entered:", currency)
    print("Amount entered:", amount)



    # ---------------- Task 2: Conversion ----------------
    if currency == "USD":
        converted_amount = amount * 132
    elif currency == "EUR":
        converted_amount = amount * 145
    elif currency == "JPY" :
        converted_amount = amount * 9.4
    elif currency == "GBP":
        converted_amount = amount * 198
    else:
        print("Unsupported currency. Conversion not possible.")
        exit()  # stop the program if invalid currency

    # Print converted amount
    print("Converted amount in NPR:", converted_amount)


    #----------------Task 4 : Transaction Report ----------
    print("\n======== Conversion History Report ========")

for i, transaction in enumerate(transactions, start=1):
    currency, amount, converted_amount = transaction
    print(f"Transaction {i}: {currency} {amount} -> NPR {converted_amount}")