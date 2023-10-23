# Generated by Django 4.2.6 on 2023-10-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_alter_booking_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=20, null=True, verbose_name='Booking Status'),
        ),
    ]
