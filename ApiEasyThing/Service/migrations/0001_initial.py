# Generated by Django 3.0.4 on 2020-03-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyId', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('typeId', models.IntegerField()),
            ],
        ),
    ]
