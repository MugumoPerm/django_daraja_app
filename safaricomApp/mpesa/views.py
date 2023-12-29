from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
import requests
import json
import base64
from datetime import datetime
import time

cl = MpesaClient()
token = cl.access_token()

# Create your views here.
def auth_token(request):
    context = { 'token': token }
    return render(request, "auth_token.html", context)


def stkpush(request):
    # Define the URL of the API endpoint
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
     # timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    business_shortcode = 110989
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
   
    # Define the data to send
    data =  {
    "BusinessShortCode": business_shortcode,
    "Password": base64.b64encode(bytes(str(business_shortcode) + str(passkey) + str(timestamp), 'utf-8')).decode('utf-8'),
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 100,
    "PartyA": 254714025354, # replace with your phone number to get stk push
    "PartyB": business_shortcode,
    "PhoneNumber": 254714025354, 
    "CallBackURL": "https://api.darajambili.com",
    "AccountReference": "perminus K Limited🔨",
    "TransactionDesc": "Lipa Deni😂" 
  }

    # Convert the data to JSON format
    json_data = json.dumps(data)


    # Create a headers dictionary with the content type, length, and authorization
    headers = {
    "Content-Type": "application/json",
    "Content-Length": str(len(json_data)),
    "Authorization": "Bearer " + token
    }

    # Send the request using requests.post and store the response
    response = requests.post(url, data=json_data, headers=headers)

    context = { "response":response.text, "time":timestamp }

    return render(request, "stkpush.html", context)
