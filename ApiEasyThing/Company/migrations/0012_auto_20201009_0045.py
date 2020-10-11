# Generated by Django 3.1.2 on 2020-10-08 21:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0011_companynews_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companynews',
            name='likes',
        ),
        migrations.AddField(
            model_name='companynews',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]