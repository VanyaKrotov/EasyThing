# Generated by Django 3.1.2 on 2020-10-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0011_auto_20201010_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='workschedule',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
