import requests,json

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/next7days?unitGroup=metric&key=PR9LZB79DX2LTEXMNHCGRTUNN&include=days,current&elements=datetime,tempmax,tempmin,temp,feelslike,sunrise,sunset,conditions,description,icon")
data = response.json()   
"""with open('api_response_chosen.json', 'w') as f:
    json.dump(data, f, indent = 4)"""

context = []
    
for day in data["days"]:
    day_info = {
    "datetime": day["datetime"],
    "tempmax": day["tempmax"],
    "tempmin": day['tempmin'],
    "temp": day["temp"],
    "feelslike": day["feelslike"],
    "sunrise": day["sunrise"],
    "sunset": day['sunset'],
    "conditions": day["conditions"],
    "description": day["description"],
    "icon": day['icon']
        }
    context.append(day_info)
print(context)
#print (data)