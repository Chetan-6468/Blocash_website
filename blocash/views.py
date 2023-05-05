from django.shortcuts import render
from django.http import HttpResponse


# Trasaction form rendering and handling
def transact(request):
    if request.method == 'POST':
        input_names = ['transaction_id', 'amount', 'payer_name', 'payer_email', 'payer_address', 'payee_name', 'payee_email', 'payee_address']
        dict_data = {}
        for i in input_names:
            data = request.POST[i]
            dict_data[i] = data
        print(dict_data)
    else:
        return render(request,"details.html")

def landing(request):
    return render(request,"Blocash.html")

def about(request):
    return render(request,"about-us.html")


def contact(request):
    return render(request,"contact-us.html")

def priv_pol(request):
    return render(request,"privacy policy.html")

def terms(request):
    return render(request,"terms&condition.html")


def blocks(request):
    return render(request,"blockchain.html")

def disc(request):
    return render(request,"disclaimer.html")

def finance_news(request):
    return render(request,"financenews.html")

def finews(request):
    return render(request,"news.html")