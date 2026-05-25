from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CurrencyConversion
import json

# Exchange rates (base: USD)
RATES = {
    "USD": 1,
    "EUR": 0.92,
    "GBP": 0.78,
    "INR": 83,
    "JPY": 150,
    "AUD": 1.52,
    "CAD": 1.36,
    "CHF": 0.88,
    "CNY": 7.2,
    "SGD": 1.34,
    "NPR": 132,
    "PKR": 278,
    "BDT": 110,
    "AED": 3.67,
    "KRW": 1330,
    "LKR": 320
}

print("API HIT")

def home(request):
    return render(request, "currency.html")
# ----------------------------
# Conversion logic (SAFE)
# ----------------------------
def convert_currency(amount, from_currency, to_currency):
    amount = float(amount)  

    from_rate = RATES[from_currency]
    to_rate = RATES[to_currency]

    base_amount = amount / from_rate
    converted = base_amount * to_rate
    rate = to_rate / from_rate

    return converted, rate


# ----------------------------
# API VIEW
# ----------------------------
@csrf_exempt
def create_conversion(request):

    # Only POST allowed
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        from_currency = data.get("from_currency")
        to_currency = data.get("to_currency")
        amount = data.get("amount")

        # ----------------------------
        # Validation
        # ----------------------------
        if not from_currency or not to_currency or amount is None:
            return JsonResponse({"error": "Missing fields"}, status=400)

        if from_currency not in RATES or to_currency not in RATES:
            return JsonResponse({"error": "Invalid currency code"}, status=400)

        # ----------------------------
        # Conversion
        # ----------------------------
        converted_amount, rate = convert_currency(amount, from_currency, to_currency)

        # ----------------------------
        # Save to DB
        # ----------------------------
        obj = CurrencyConversion.objects.create(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=float(amount),  
            converted_amount=converted_amount,
            conversion_rate=rate
        )

        # ----------------------------
        # Response
        # ----------------------------
        return JsonResponse({
            "message": "Conversion successful",
            "id": obj.id,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": float(amount),
            "converted_amount": converted_amount,
            "conversion_rate": rate
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def get_all_conversion(request):
    if request.method == "GET":
        data = list(CurrencyConversion.objects.values())
        return JsonResponse(data,safe=False)

# ----------------------------------------------
#Read One
#-----------------------------------------------

def get_single_conversion(request,id):
    if request.method == "GET" :
        obj = CurrencyConversion.objects.get(id=id)

        return JsonResponse({
            "id" : obj.id,
            "from_currency" : obj.from_currency,
            "to_currency": obj.to_currency,
            "amount" : obj.amount,
            "conversion_amount": obj.amount,
            "conversion_rate" :obj.conversion_rate


        })


@csrf_exempt   
def update_conversion(request,id):
    if request.method == "PUT":
        data =json.loads(request.body)
        obj = CurrencyConversion.objects.get(id=id)
        obj.from_currency = data.get("from_currency",obj.from_currency)
        obj.to_currency = data.get("to_currency",obj.to_currency)
        obj.amount = float(data.get("amount",obj.amount))

        obj.save()
        return JsonResponse({"message":"Updated"})


#delete
def delete_conversion(request,id):
    if request.method == "Delete":
        obj = CurrencyConversion.objects.get(id=id)
        obj.delete()

        return JsonResponse({"message": "deleted"})