# Generated by Django 4.2.3 on 2023-07-13 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0009_alter_vehicles_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='make_id',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='model',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='model_id',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='year',
        ),
    ]