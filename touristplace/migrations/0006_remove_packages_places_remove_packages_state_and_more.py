# Generated by Django 4.2.6 on 2023-10-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touristplace', '0005_state_alt_state_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='places',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='state',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Packages',
        ),
    ]
