# Generated by Django 3.1.1 on 2020-09-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200913_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='invite_reason',
        ),
        migrations.AddField(
            model_name='membership',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
