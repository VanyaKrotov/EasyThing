# Generated by Django 3.1.2 on 2020-10-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0013_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/service/'),
        ),
    ]