# Generated by Django 3.0.4 on 2020-04-11 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0004_auto_20200329_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('permissions', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company', verbose_name='news')),
            ],
        ),
    ]
