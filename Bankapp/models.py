from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    customer_id = models.IntegerField()
    transaction_date = models.DateField()
    amount=models.IntegerField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sname = models.CharField(max_length=122)
    rname = models.CharField(max_length=122)
    money=models.IntegerField()
    tdate = models.DateTimeField()

    def __str__(self):
        return self.sname