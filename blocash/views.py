from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . forms import ContactForm
from django.contrib.auth import login,logout
import json,hashlib,secrets,string

# Trasaction form rendering and handling
def transact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            input_names = ['transaction_id', 'amount', 'payer_name', 'payer_email', 'payer_address', 'payee_name', 'payee_email', 'payee_address','value']
            dict_data = {}
            for i in input_names:
                data = request.POST[i]
                dict_data[i] = data
            print(dict_data)
            # Define transaction details
            transaction = {
                "transaction_id": dict_data['transaction_id'],
                "amount": dict_data['amount'],
                "payer": {
                    "name": dict_data['payer_name'],
                    "email": dict_data['payer_email'],
                    "address": dict_data['payer_address']
                },
                "payee": {
                    "name": dict_data['payee_name'],
                    "email": dict_data['payee_email'],
                    "address": dict_data['payee_address']
                }
            }
                    
            # Convert transaction to a JSON string
            transaction_string = json.dumps(transaction)

            # Generate SHA256 hash of the transaction string
            hash_object = hashlib.sha256()
            hash_object.update(transaction_string.encode('utf-8'))
            hash_value = hash_object.hexdigest()
            return HttpResponse(str(dict_data.values())+"\n"+hash_value)
        else:
            # Define the length of the random string
            length = 32
            # Define the character set to choose from
            charset = string.ascii_letters + string.digits
            # Generate the random string
            random_string = ''.join(secrets.choice(charset) for i in range(length)).upper()

            return render(request,"details.html",{'transaction_id':random_string})
    else:
        return HttpResponse("You are not logged in")

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

def register(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'password1': request.POST['password1'],
            'password2': request.POST['password2']
        }
        
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved Successfully")
        else:
            return render(request,"register.html",{'error':form.errors})
    else:
        user_form = UserCreationForm()
        return render(request, "register.html", {'form': user_form})

def logon(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'password': request.POST['password']
        }
        form = AuthenticationForm(request,data)

        if form.is_valid():
            user = User.objects.filter(username=data['username'])[0]
            login(request,user)
            return redirect('/profile/')
        else :
            return HttpResponse(form.errors)
    else :
        user_login = AuthenticationForm()
        return render(request,"login.html",{'form':user_login})
    
def logoff(request):
    logout(request)
    return redirect("/")
    
def profile(request):
    if request.user.is_authenticated :
        form = ContactForm()
        return render(request,"profile.html",{'form':form})
    else :
        return redirect("/login/")