# Generated by Django 4.2.6 on 2023-10-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touristplace', '0008_touristplaceimage_google_map_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristplaceimage',
            name='google_map_src',
        ),
        migrations.AddField(
            model_name='touristplace',
            name='google_map_src',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
