from .models import Ticket
from random import choice
from string import ascii_uppercase, digits
import random
import datetime

def PopulateDb():
    cities = ["Rome", "Madrid","London", "Venice", "Milan", "Moscow", "New York", "San Francisco", "Berlin"]

    #random creation of 5 flight
    for x in range(5):
        ticket = Ticket(
            departure_city = cities[random.randint(0, 8)],
            arrival_city = cities[random.randint(0, 8)],
            price = random.randint(50, 200), 
            date_departure = datetime.date.today() + datetime.timedelta(days=random.randint(0, 50)),
            airplane_code = ("".join(choice(ascii_uppercase + digits) for i in range(5))),
            code = ("".join(choice(ascii_uppercase + digits) for i in range(5)))
        )
        ticket.save()
