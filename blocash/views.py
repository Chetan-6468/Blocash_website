from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . forms import ContactForm,User_Detail
from models.models import Wallet,Transaction
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json,hashlib,secrets,string,requests,json,base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

@login_required
def transact(request):
    if request.method == 'POST':
        input_names = ['transaction_id', 'amount', 'payer_name', 'payer_email', 'payer_address', 'payee_name', 'payee_email', 'payee_address','value']
        dict_data = {}
        for i in input_names:
            data = request.POST[i]
            dict_data[i] = data
        # Replace this with the exported key from JavaScript
        # Base64-decode the exported JWK
        jwk_str = dict_data['value'] # replace with the exported JWK
        jwk_json = base64.urlsafe_b64decode(jwk_str + "===")
        jwk = json.loads(jwk_json)

        # Extract the key parameters from the JWK
        key_bytes = base64.urlsafe_b64decode(jwk['k'])
        iv = base64.urlsafe_b64decode(jwk['iv'])
        tag = base64.urlsafe_b64decode(jwk['alg'].split('.')[2])
        salt = base64.urlsafe_b64decode(jwk['kdf']['salt'])
        iterations = jwk['kdf']['iter']
        key_length = len(key_bytes) * 8

        # Derive the key from the password using PBKDF2
        password = dict_data['pass'] # replace with the password used to generate the key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=key_length//8,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        # Initialize the cipher with the key, IV, and tag
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())

        # Decrypt the ciphertext
        ciphertext = dict_data['amount'] # replace with the base64-encoded ciphertext
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

@login_required
def wallet(request):
    user = User.objects.filter(username=request.user.username)[0]
    balance = Wallet.objects.filter(user=user)[0].balance
    transactions = Transaction.objects.filter(user=user)
    return render(request,"wallet.html",{'balance':balance,'transactions':transactions})

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
    API_KEY = "pub_21771e76a72126f950e9aa28961d45d53be97"
    URL = "https://newsdata.io/api/1/news?apikey=pub_21771e76a72126f950e9aa28961d45d53be97&q=pegasus&language=en"

    res = requests.get(URL)
    json_res = res.json()
    news_array = json_res['results']
    return render(request,"news.html",{'news':news_array})

def register(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'first_name' : request.POST['fname'],
            'last_name' : request.POST['lname'],
            'email' : request.POST['email'],
            'password1': request.POST['password1'],
            'password2': request.POST['password2']
        }
    
        form = UserCreationForm(data)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            user_obj = User.objects.filter(username=data['username'])[0]
            Wallet.objects.create(
                balance = 100.00,
                user = user_obj
            )
            message = "You are registered successfully!"
            messages.success(request, message)
            return render(request, "login_form.html")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "register_form.html")
    else:
        return render(request, "register_form.html")

def logon(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'password': request.POST['password']
        }

        if authenticate(**data):
            user = User.objects.filter(username=data['username'])[0]
            login(request,user)
            messages.success(request,"You are success fully logged in !!")
            return redirect('/profile/')
        else:
            messages.error(request,"Incorrect username or password !!")
            return render(request,"login_form.html")
    else :
        return render(request,"login_form.html")

@login_required    
def logoff(request):
    logout(request)
    return redirect("/")
    
@login_required
def profile(request):
    my_user = User.objects.filter(username = str(request.user.username))[0]
    name = my_user.first_name + " " + my_user.last_name
    return render(request,"dashboard.html",{'name':name.upper()})
