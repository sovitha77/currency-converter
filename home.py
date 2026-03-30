# """TASK 1:
# Program: Currency Input Program
# Objective:
# This program asks the user to enter a currency type and an amount.
# It checks if the amount entered is a valid number.
# Then it displays the currency and amount entered by the user.
# # # """
from psycopg2 import connect

# transactions = []
# for i in range(4):  #task-3 as loop is said to be applied in the  same process as the task 1 and 2 

#     # Ask the user to enter the currency type
#     currency = input("Enter currency (USD or EUR or JPY or GBP): ")

#     # Ask the user to enter the amount
#     amount = float(input("Enter amount: "))
#     print("Currency entered:", currency)
#     print("Amount entered:", amount)



#     # ---------------- Task 2: Conversion ----------------
#     if currency == "USD":
#         converted_amount = amount * 132
#     elif currency == "EUR":
#         converted_amount = amount * 145
#     elif currency == "JPY" :
#         converted_amount = amount * 9.4
#     elif currency == "GBP":
#         converted_amount = amount * 198
#     else:
#         print("Unsupported currency. Conversion not possible.")
#         exit()  # stop the program if invalid currency

#         print("Converted amount")
#         print("Converted amount in NPR:", converted_amount)
     



# """
# Program: Currency Converter
# Description: This program defines a function convert_currency(amount, rate)
# that converts a foreign currency amount into Nepalese Rupees (NPR)
# using a given exchange rate.
# """

# def convert_currency(amount, rate):
#     """
#     This function converts foreign currency to NPR.
    
#     Parameters:
#     amount : float -> foreign currency amount
#     rate   : float -> exchange rate to NPR
    
#     Returns:
#     float -> converted amount in NPR
#     """
    
#     npr = amount * rate
#     return npr


# # Example usage
# foreign_amount = 100      # Example foreign currency amount
# exchange_rate = 133.5     # Example rate (1 unit foreign currency = 133.5 NPR)

# result = convert_currency(foreign_amount, exchange_rate)

# print("Converted amount in NPR:", result)

from db import connect_db   # import from db.py

# -------------------------------
# Part 1: Input Storage
# -------------------------------
conversion_request = []
unique_currencies = set()
currency_count = {}

# -------------------------------
# Part 2: Conversion Logic
# -------------------------------
exchange_rates = [
    ("USD", "NPR", 132),
    ("INR", "NPR", 1.6),
    ("EUR", "NPR", 145),
    ("GBP", "NPR", 198),
    ("JPY", "NPR", 9.4)
]

def get_rate_to_npr(source):
    for rate in exchange_rates:
        if rate[0] == source:
            return rate[2]
    return None


# -------------------------------
# Create Table
# -------------------------------
def create_table():
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS conversions (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        currency VARCHAR(10),
        amount FLOAT,
        converted_amount FLOAT
    );
    """

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()


# -------------------------------
# Insert into Database
# -------------------------------
def insert_conversion(name, currency, amount, result):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO conversions (name, currency, amount, converted_amount)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, currency, amount, result))
    conn.commit()

    cursor.close()
    conn.close()


# -------------------------------
# Add Conversion Request
# -------------------------------
def add_conversion_request():
    name = input("Enter your name: ")
    source = input("Enter source currency (USD, INR, EUR, GBP, JPY): ").upper()
    amount = float(input("Enter amount to convert: "))

    rate = get_rate_to_npr(source)

    if rate is None:
        print("Currency not supported.\n")
        return

    converted_amount = amount * rate

    request = {
        "Name": name,
        "Source": source,
        "Target": "NPR",
        "Amount": amount
    }

    conversion_request.append(request)

    unique_currencies.add(source)
    currency_count[source] = currency_count.get(source, 0) + 1

    # Save to DATABASE instead of file
    insert_conversion(name, source, amount, converted_amount)

    print(f"{name} converted {amount} {source} to {converted_amount:.2f} NPR\n")


# -------------------------------
# Conversion Report
# -------------------------------
def print_conversion_report():
    if not conversion_request:
        print("No conversions to display.\n")
        return

    print("\n---- Conversion Logs ----")
    for req in conversion_request:
        converted_amount = req["Amount"] * get_rate_to_npr(req["Source"])
        print(req["Name"], "converted", req["Amount"], req["Source"], "to", converted_amount, "NPR")

    most_used = max(currency_count, key=currency_count.get)
    print("\nMost Used Currency:", most_used)
    print("Unique Currencies:", unique_currencies)


# -------------------------------
# Main Program
# -------------------------------

create_table()

while True:
    try:
        num_request = int(input("How many conversions do you want to enter? "))
        break
    except ValueError:
        print("Please enter a valid number!")

for i in range(num_request):
    add_conversion_request()

print_conversion_report()