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