# Generated by Django 3.0.4 on 2020-04-11 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0006_auto_20200411_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companynews',
            name='date',
        ),
        migrations.AddField(
            model_name='companynews',
            name='dateCreate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 11, 10, 4, 3, 816289, tzinfo=utc)),
            preserve_default=False,
        ),
    ]