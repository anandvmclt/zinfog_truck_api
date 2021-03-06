# Generated by Django 3.0.9 on 2020-08-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=100)),
                ('pickUpFrom', models.CharField(blank=True, max_length=100)),
                ('deliveryTo', models.CharField(blank=True, max_length=100)),
                ('yourName', models.CharField(blank=True, max_length=100)),
                ('emailId', models.EmailField(blank=True, max_length=120)),
                ('phoneNo', models.CharField(blank=True, max_length=25)),
                ('truckType', models.CharField(blank=True, max_length=100)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
