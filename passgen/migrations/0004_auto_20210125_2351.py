# Generated by Django 3.1.5 on 2021-01-25 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passgen', '0003_password_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='profile_user',
        ),
        migrations.AddField(
            model_name='password',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cpg_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
