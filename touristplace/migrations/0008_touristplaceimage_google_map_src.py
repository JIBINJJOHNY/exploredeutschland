# Generated by Django 4.2.6 on 2023-10-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touristplace', '0007_alter_rev_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristplaceimage',
            name='google_map_src',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
