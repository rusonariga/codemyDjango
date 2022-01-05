from django.shortcuts import render


def home(request):
    import requests
    import json
    # pk_9c23b434f75d428eb7753d06ca042844
    api_request = requests.get(
        "https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_9c23b434f75d428eb7753d06ca042844")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
