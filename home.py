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

    #Print converted amount
    print("Converted amount in NPR:", converted_amount)


    #----------------Task 4 : Transaction Report ----------
    print("\n======== Conversion History Report ========")

for i, transaction in enumerate(transactions, start=1):
    currency, amount, converted_amount = transaction
    print(f"Transaction {i}: {currency} {amount} -> NPR {converted_amount}")


"""
Program: Currency Converter
Description: This program defines a function convert_currency(amount, rate)
that converts a foreign currency amount into Nepalese Rupees (NPR)
using a given exchange rate.
"""

def convert_currency(amount, rate):
    """
    This function converts foreign currency to NPR.
    
    Parameters:
    amount : float -> foreign currency amount
    rate   : float -> exchange rate to NPR
    
    Returns:
    float -> converted amount in NPR
    """
    
    npr = amount * rate
    return npr


# Example usage
foreign_amount = 100      # Example foreign currency amount
exchange_rate = 133.5     # Example rate (1 unit foreign currency = 133.5 NPR)

result = convert_currency(foreign_amount, exchange_rate)

print("Converted amount in NPR:", result)

#Tasks 2 Creating function get_currency_rate(currency) that returns the conversion rate based on the currency type

def get_currency_rate(current):
    if currency == "USD":
        return 132
    elif currency == "EUR":
        return 145
    elif currency == "INR":
        return 1.6
    elif currency == "JPY":
        return 9.4
    elif currency == "GBP":
        return 198
    else :
        print("Unsupported currency ")
        return None
    
#Task 3 Create a function save_conversion(currency, amount, result) that saves conversion history in currency_history.txt.

def save_conversion(currency, amount, result):

    file = open("currency_history.txt", "a")

    file.write(f"{currency} {amount} -> NPR {result}\n")

    file.close()

