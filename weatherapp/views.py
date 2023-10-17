from django.shortcuts import render
import requests
import datetime

# Create your views here.

def home(request):
    if 'locationinput' in request.POST:
        locationinput = request.POST['locationinput']
    else:
        locationinput = 'Nairobi'
    URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
    api_key = 'FQUQ9VQWFS6QJWJ9RYG6NGKJC'
    params = {"location":locationinput,"key": api_key,"unitGroup": "metric"}
    resp = requests.get(URL,params).json()
    cond = resp["description"]
    timez = resp["timezone"]
    date = datetime.datetime.today()
    current = resp["currentConditions"]["temp"]
    return render(request,'home.html',{"location": locationinput,"conditions": cond,"timezone":timez,"date":date,"currentweather":current})
