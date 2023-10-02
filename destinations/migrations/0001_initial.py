# Generated by Django 4.2.5 on 2023-10-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required. Max length: 100 characters', max_length=100, unique=True, verbose_name='Destination Name')),
                ('description', models.TextField(help_text='Required', verbose_name='Destination Description')),
                ('location', models.CharField(help_text='Required. Max length: 100 characters', max_length=100, verbose_name='Destination Location')),
                ('slug', models.SlugField(help_text='Required. Max length: 150 characters', max_length=150, unique=True, verbose_name='Destination Slug')),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
                'ordering': ['name'],
            },
        ),
    ]