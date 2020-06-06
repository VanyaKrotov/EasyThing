# Generated by Django 3.0.4 on 2020-03-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterId', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('dateCreated', models.DateField()),
                ('dateRegistration', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
