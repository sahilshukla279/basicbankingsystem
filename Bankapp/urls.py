from django.contrib import admin
from django.urls import path
from Bankapp import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about", views.about, name="about"),
    path("view_customer", views.view_customer, name="view_customer"),
    path("make_transaction", views.make_transaction, name="make_transaction"),
    path("history", views.history, name="history")

]
