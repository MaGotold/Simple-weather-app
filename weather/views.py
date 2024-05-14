from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
from django.views.generic.base import TemplateView
from dotenv import load_dotenv
load_dotenv()
import os
# Create your views here.

def call_api(request):
    
    if request.method == "GET":
        location = request.GET.get("location")
        
    api_key = os.environ.get('API_KEY')
    if location:
        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next7days?unitGroup=metric&key={api_key}&include=days,current&elements=datetime,tempmax,tempmin,temp,feelslike,sunrise,sunset,conditions,description,icon")
    else : response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Považská Bystrica/next7days?unitGroup=metric&key={os.environ.get(api_key)}&include=days,current&elements=datetime,tempmax,tempmin,temp,feelslike,sunrise,sunset,conditions,description,icon")

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
    return render(request,"index.html",{"data" : data,"context":context})




class DaysView(TemplateView):
    template_name = "days.html"
    
    def call_api():
        response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Považská Bystrica/next7days?unitGroup=metric&key=PR9LZB79DX2LTEXMNHCGRTUNN&include=days,current&elements=datetime,tempmax,tempmin,temp,feelslike,sunrise,sunset,conditions,description,icon")
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
        return context,data


    
