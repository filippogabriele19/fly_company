from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile, Ticket
from .forms import SignUpForm
from .createdefaultdata import PopulateDb
from datetime import datetime
import smart_contract.interact_with_rome_ny as contract
import os

# variable used for pass message through functions
message = ""


def home_view(request):
    # take all available flight
    print("-----------------------------------------------------------------------1")
    all_tickets = Ticket.objects.all().order_by("date_departure")
    Ticket.objects.all().delete()
    if all_tickets.count() == 0:
        # if it is empty they will be generated
        PopulateDb()

    all_tickets = Ticket.objects.all().order_by("date_departure")

    my_mess = ""
    global message
    if message != "":
        my_mess = message
        message = ""

    print(all_tickets)
    return render(request, "home.html", {"tickets": all_tickets, "message": my_mess})


def signup_view(request):
    # registration form
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get("first_name")
            user.profile.last_name = form.cleaned_data.get("last_name")
            user.profile.email = form.cleaned_data.get("email")
            user.is_active = True
            user.save()

            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def ticket_detail_view(request, pk):
    # open detail of available ticket to buy
    ticket = get_object_or_404(Ticket, pk=pk)
    address = contract.return_contract_address()
    return render(request, "ticket_detail.html", {"ticket": ticket, "address": address})


def search_ticket_from_code_view(request):
    if request.method == "GET":
        codeInput = request.GET["code"]
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def add_new_ticket_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    check_bool = contract.buy_nft()
    global message
    if check_bool == True:
        message = "All gone well!"
    else:
        message = "Some error occurs"

    return HttpResponseRedirect("/")
