# Generated by Django 4.0.5 on 2022-06-29 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
