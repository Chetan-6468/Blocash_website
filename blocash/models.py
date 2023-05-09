from django.db import models
from django.contrib.auth.models import User

# class Transaction(models.Model):
#     pass


class User_Detail(models.Model):
    uid = models.CharField(max_length=50,blank=False,default="None")
    fname = models.CharField(max_length=50,blank=False,default="None")
    mname = models.CharField(max_length=50,default="None")
    lname = models.CharField(max_length=50,blank=False,default="None")
    email = models.EmailField()

    def __str__(self) -> str:
        return self.uid


# Please Enter Nuts Under Machine As Brother Crying Lot