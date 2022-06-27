from .models import Ticket
import random
import datetime


def PopulateDb():
    ticket = Ticket(
        departure_city="Rome",
        arrival_city="New York",
        date_departure=datetime.date.today()
        + datetime.timedelta(days=random.randint(0, 50)),
    )
    ticket.save()
