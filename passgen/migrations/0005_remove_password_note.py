# Generated by Django 3.1.5 on 2021-01-25 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passgen', '0004_auto_20210125_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='note',
        ),
    ]
