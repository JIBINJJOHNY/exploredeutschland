# Generated by Django 4.2.6 on 2023-10-09 21:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touristplace', '0003_alter_touristplace_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_days', models.IntegerField(choices=[(1, '1 Day'), (2, '2 Days')], verbose_name='Packages Days')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('places_limit', models.IntegerField(choices=[(1, '3 Places (1 Day)'), (2, '6 Places (2 Days)')], verbose_name='Places Limit')),
                ('places', models.ManyToManyField(help_text='Select tourist places for this package', to='touristplace.touristplace', verbose_name='Tourist Places')),
                ('state', models.ForeignKey(help_text='Choose the state for this package', on_delete=django.db.models.deletion.CASCADE, to='touristplace.state', verbose_name='State')),
            ],
            options={
                'verbose_name': 'Packages',
                'verbose_name_plural': 'Packages',
                'ordering': ['state', 'package_days'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Select the booking date', verbose_name='Booking Date')),
                ('no_of_guests', models.IntegerField(help_text='Enter the number of guests (maximum 6)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Number of Guests')),
                ('package', models.ForeignKey(help_text='Select the package for the booking', on_delete=django.db.models.deletion.CASCADE, to='touristplace.packages', verbose_name='Packages')),
                ('user', models.ForeignKey(help_text='Select the user making the booking', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ['date'],
            },
        ),
    ]
