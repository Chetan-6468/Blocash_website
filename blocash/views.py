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
from cryptography.hazmat.primitives import hashes,padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def decrypt_aes_gcm(ciphertext, key, iv, aad=None,tag=None):
    # Create AES-GCM cipher with the provided key
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv,tag))

    # Create a decryptor object
    decryptor = cipher.decryptor()

    # Set associated data (if provided)
    if aad:
        decryptor.authenticate_additional_data(aad)

    # Decrypt the ciphertext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext


@login_required
def transact(request):
    if request.method == 'POST':
        input_names = ['transaction_id', 'amount', 'payer_name', 'payer_email', 'payer_address', 'payee_name', 'payee_email', 'payee_address', 'key','iv']
        dict_data = {}
        for i in input_names:
            data = request.POST[i]
            dict_data[i] = data
        
        recv_hash = request.POST['hash']

        value_json = dict_data['key']
        value_dict = json.loads(value_json)
        key_bytes = base64.urlsafe_b64decode(value_dict['k']+'==')
        
        iv_json = dict_data['iv']
        iv_dict = json.loads(iv_json)
        iv_bytes = bytes(iv_dict.values())

        del dict_data['key'] 
        del dict_data['iv']
        data = {}
        keys = dict_data.keys()

        for key in keys :

            cipher_text = dict_data[key]
            cipher_bytes = base64.urlsafe_b64decode(cipher_text)

            # Ensure cipher_bytes is a byte-like object
            if isinstance(cipher_bytes, str):
                cipher_bytes = cipher_bytes.encode('utf-8')

            tag = cipher_bytes[-16:]
            cipher_without_tag = cipher_bytes[:-16]

            
            data[key] = decrypt_aes_gcm(cipher_without_tag,key_bytes,iv_bytes,tag=tag)

            # Define transaction details
            transaction = {
                "transaction_id": data['transaction_id'],
                "amount": data['amount'],
                "payer": {
                    "name": data['payer_name'],
                    "email": data['payer_email'],
                    "address": data['payer_address']
                },
                "payee": {
                    "name": data['payee_name'],
                    "email": data['payee_email'],
                    "address": data['payee_address']
                }
            }

            json_data = json.dumps(transaction)
            
            # Generate SHA256 hash of the transaction string
            hash_object = hashlib.sha256()
            hash_object.update(json_data.encode('utf-8'))
            hash_value = hash_object.hexdigest()

        print(recv_hash,hash_value)

        return HttpResponse(data.values())
    else:
        # Handle GET request
        alphabet = string.ascii_letters + string.digits
        transaction_id =  ''.join(secrets.choice(alphabet) for _ in range(24))

        return render(request,"details.html",{'transaction_id':transaction_id.upper()})
        
@login_required
def wallet(request):
    user = User.objects.filter(username=request.user.username)[0]
    user_inst = Wallet.objects.filter(user=user)[0]
    balance = user_inst.balance
    wallet_addr = user_inst.wallet_address
    transactions = Transaction.objects.filter(user=user)
    return render(request,"wallet.html",{'balance':balance,'transactions':transactions,'wallet_addr': wallet_addr})

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
            # Handle GET request
            alphabet = string.ascii_letters + string.digits
            random_str =  ''.join(secrets.choice(alphabet) for _ in range(24))
            Wallet.objects.create(
                wallet_address = random_str.upper(),
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
    wallet_addr = Wallet.objects.filter(user=my_user)[0].wallet_address
    return render(request,"dashboard.html",{'name':name.upper(),'wallet_addr':wallet_addr})
