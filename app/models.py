from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djongo.models.fields import ObjectIdField


class Profile(models.Model):
    _id = ObjectIdField()
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Ticket(models.Model):
    customer_name = models.CharField(max_length=15, blank=True)
    customer_last_name = models.CharField(max_length=15, blank=True)
    date_purchase = models.DateTimeField(auto_now_add=True)
    date_departure = models.DateTimeField()
    departure_city = models.CharField(max_length=15, blank=True)
    arrival_city = models.CharField(max_length=15, blank=True)
    price = models.IntegerField()
    airplane_code = models.CharField(max_length=5, blank=True)
    code = models.CharField(max_length=5, blank=True)
