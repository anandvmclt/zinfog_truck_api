# Generated by Django 3.1 on 2020-08-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0006_auto_20200810_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
