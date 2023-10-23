# Generated by Django 4.2.6 on 2023-10-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='contact_email',
            field=models.EmailField(help_text='Enter the contact email address', max_length=254, verbose_name='Contact Email'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('online', 'Online Payment'), ('cash', 'Cash Payment')], max_length=50, verbose_name='Payment Method'),
        ),
    ]
