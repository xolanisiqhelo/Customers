# Generated by Django 2.0.1 on 2019-09-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20190926_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='custFirstName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='custLastname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customerCode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='deliveryaddress',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='statusCode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='statusDescription',
        ),
    ]
