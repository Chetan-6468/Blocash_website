from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    # Fields for the Transaction model
    tid = models.CharField(max_length=24,default="None")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    from_account = models.CharField(max_length=255)
    to_account = models.CharField(max_length=255)
    
    # Relationship fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.timestamp} - {self.description} - {self.amount} - From: {self.from_account} - To: {self.to_account}"


class Wallet(models.Model):
    # Fields for the Wallet model
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet - Balance: {self.balance}"

# Please Enter Nuts Under Machine As Brother Crying Lot
