# Generated by Django 4.2.16 on 2024-12-21 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
