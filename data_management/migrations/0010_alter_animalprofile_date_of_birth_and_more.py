# Generated by Django 4.2.16 on 2025-01-08 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0009_alter_animalprofile_livestock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='date_weighted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='deathrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='death_records', to='data_management.animalprofile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_records', to='data_management.animalprofile'),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_records', to='data_management.animalprofile'),
        ),
        migrations.AlterField(
            model_name='vaccinationrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vaccination_records', to='data_management.animalprofile'),
        ),
    ]
