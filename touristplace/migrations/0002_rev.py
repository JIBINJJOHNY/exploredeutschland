# Generated by Django 4.2.6 on 2023-10-09 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touristplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tourist_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revs', to='touristplace.touristplace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
