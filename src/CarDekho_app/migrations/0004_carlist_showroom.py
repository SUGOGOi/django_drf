# Generated by Django 5.0.6 on 2024-07-04 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0003_showroomlist_alter_carlist_chassisnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Showrooms', to='CarDekho_app.showroomlist'),
        ),
    ]
