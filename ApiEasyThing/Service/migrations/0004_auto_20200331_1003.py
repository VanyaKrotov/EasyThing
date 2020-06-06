# Generated by Django 3.0.4 on 2020-03-31 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_auto_20200329_1653'),
        ('Service', '0003_auto_20200331_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='Company.Company'),
        ),
        migrations.AlterField(
            model_name='service',
            name='parentService',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='Service.Service'),
        ),
    ]