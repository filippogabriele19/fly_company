# Generated by Django 2.2 on 2022-05-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220510_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='profile',
        ),
        migrations.AddField(
            model_name='ticket',
            name='customer_last_name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='ticket',
            name='customer_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]