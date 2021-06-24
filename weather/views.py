from django.shortcuts import render
import requests
from .forms import SearchForm
from django.contrib import messages
# Create your views here.

def home(request):
    forms = SearchForm()

    # if request.method == 'POST':
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b9ed7912a62809df13101361cc25b375'
    city = request.GET.get('search')
    print(city)
    r = requests.get(url.format(city)).json()
    if r['cod'] == '404':
        messages.warning(request, "City not found")
    else:
        tempareture = r['main']['temp']
        des = r['weather'][0]['description']
        icon = r['weather'][0]['icon']
        city_name = r['name']
        country = r['sys']['country']
        context ={
            'forms':forms,
            'tempareture': tempareture,
            'des':des,
            'icon':icon,
            'city_name': city_name,
            'country': country
        }
        return render(request, 'home.html', context)
    context ={
            'forms':forms,
            'tempareture': 'Fill The Searchbar',
            'des':'Fill The Searchbar',
            'icon':'icon',
            'city_name': 'Fill The Searchbar',
            'country': 'Fill The Searchbar'
        }
    return render(request, 'home.html', context)