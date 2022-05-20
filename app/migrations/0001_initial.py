# Generated by Django 2.2 on 2022-05-02 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('usd', models.FloatField(default=1000)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('private_key', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchase', models.DateTimeField(auto_now_add=True)),
                ('date_departure', models.DateTimeField()),
                ('price', models.FloatField()),
                ('code', models.CharField(blank=True, max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile')),
            ],
        ),
    ]