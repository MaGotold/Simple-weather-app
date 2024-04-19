from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
# Create your views here.

def call_api(request):
    
    if request.method == "GET":
        location = request.GET.get("location")
        
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next7days?unitGroup=metric&key=PR9LZB79DX2LTEXMNHCGRTUNN&include=days,current&elements=datetime,tempmax,tempmin,temp,feelslike,sunrise,sunset,conditions,description,icon")
    data = response.json() 
    context = []
    
    for day in data["days"][1:]:
        day_info = {
            "datetime": datetime.strptime(day["datetime"],"%Y-%m-%d"),
            "tempmax": round(day["tempmax"]),
            "tempmin": round(day['tempmin']),
            "temp": day["temp"],
            "feelslike": day["feelslike"],
            "sunrise": day["sunrise"],
            "sunset": day['sunset'],
            "conditions": day["conditions"],
            "description": day["description"],
            "icon": day['icon']
        }
        context.append(day_info)
    return render(request,"base.html",{"data" : data,"context":context})
    
