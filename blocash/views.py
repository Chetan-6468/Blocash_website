from django.shortcuts import render
from django.http import HttpResponse


# Trasaction form rendering and handling
def transact(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,"index.html")

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