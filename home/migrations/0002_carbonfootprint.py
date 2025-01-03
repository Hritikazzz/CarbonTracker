# Generated by Django 4.2.17 on 2025-01-01 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonFootprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity', models.FloatField(default=0.0)),
                ('natural_gas', models.FloatField(default=0.0)),
                ('heating_oil', models.FloatField(default=0.0)),
                ('coal', models.FloatField(default=0.0)),
                ('lpg', models.FloatField(default=0.0)),
                ('propane', models.FloatField(default=0.0)),
                ('wood', models.FloatField(default=0.0)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
