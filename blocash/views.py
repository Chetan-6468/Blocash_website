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