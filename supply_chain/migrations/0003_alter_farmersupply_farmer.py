# Generated by Django 4.2.16 on 2024-12-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
        ('supply_chain', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmersupply',
            name='farmer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_management.farmer'),
        ),
    ]
