"""
URL configuration for blocash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.logon,name='login'),
    path('logoff/',views.logoff,name='logoff'),
    path('about-us/',views.about,name='about'),
    path('disc/',views.disc,name='disc'),
    path('finews/',views.finews,name='finews'),
    path('wallet/',views.wallet,name='wallet'),
    path('priv_pol/',views.priv_pol,name='privacy'),
    path('t&c/',views.terms,name='terms'),
    path('blockchain/',views.blocks,name='blockchain'),
    path('finance_news/',views.finance_news,name='finance_news'),
    path('contact/',views.contact,name='contact-us'),
    path('transact/',views.transact,name='transact'),
]
# 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