# Generated by Django 4.2.17 on 2025-01-01 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_carbonfootprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbonfootprint',
            name='total_footprint',
            field=models.FloatField(default=0.0),
        ),
    ]