# Generated by Django 3.0.4 on 2020-04-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
        ('Workers', '0002_auto_20200418_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhistory',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='Department.Department'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
