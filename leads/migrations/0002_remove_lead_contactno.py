# Generated by Django 4.1 on 2022-09-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='contactno',
        ),
    ]
