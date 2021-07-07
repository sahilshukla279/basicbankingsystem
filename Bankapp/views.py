from django.shortcuts import render, HttpResponse
from Bankapp.models import Customer, Transaction
from django.contrib import messages
from django.db.models import F
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def view_customer(request):
    customer = Customer.objects.all()
    if request.method == 'POST':
        if request.POST.get('name'):
            name = request.POST.get('name')
            cust = Customer.objects.get(name=name)
            return render(request,'view_customer.html',{'cv':cust, 'vc': customer})
        else:
            return render(request,'view_customer.html',{'vc':customer})
    else:
        return render(request,'view_customer.html',{'vc':customer}) 

    
def make_transaction(request):
    customer = Customer.objects.all()
    if request.method == 'POST':
        sname = request.POST.get('sname')
        rname = request.POST.get('rname')
        money = float(request.POST.get('amount'))
        scust = Customer.objects.get(name=sname)
        scust.amount = (scust.amount-money)
        scust.save()
        rcust = Customer.objects.get(name=rname)
        rcust.amount = (rcust.amount+money)
        rcust.save()    
        transfer = Transaction(sname=sname,rname=rname,money=money,tdate=datetime.today())
        transfer.save()
        messages.success(request, 'Your Money has been successfully Transfered!!!')
        return render(request, 'make_transaction.html')

    else:
        return render(request,'make_transaction.html',{'vc':customer})
    
def history(request):
    transaction = Transaction.objects.all()
    return render(request,'history.html',{'tc':transaction})
    
