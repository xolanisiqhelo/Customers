# Generated by Django 2.2.5 on 2019-09-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190925_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeReference',
            fields=[
                ('statusCode', models.IntegerField(help_text='Primary key Unique identifier', primary_key=True, serialize=False)),
                ('description', models.CharField(help_text='Verbose description related to the StatusCode', max_length=100)),
            ],
        ),
    ]
