# Generated by Django 5.0.6 on 2024-07-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chassisnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
