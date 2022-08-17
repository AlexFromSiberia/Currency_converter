from django.shortcuts import render
import requests


def index(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {'currencies': currencies}

        return render(request, 'app/index.html', context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr] * float(from_amount)), 2)

        context = {'currencies': currencies,
                   'converted_amount': converted_amount,
                   'from_amount': from_amount,
                   'from_curr': from_curr,
                   'to_curr': to_curr}
        return render(request, 'app/index.html', context)
