# Generated by Django 4.2.16 on 2025-01-05 17:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0004_remove_livestock_breed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalprofile',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='event',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='healthrecord',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='milkproduction',
            name='livestock',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='livestock',
        ),
        migrations.AddField(
            model_name='animalprofile',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deathrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='death_record', to='data_management.animalprofile'),
        ),
        migrations.AddField(
            model_name='deathrecord',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_record', to='data_management.animalprofile'),
        ),
        migrations.AddField(
            model_name='event',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_record', to='data_management.animalprofile'),
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milk_records', to='data_management.animalprofile'),
        ),
        migrations.AddField(
            model_name='vaccinationrecord',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vaccination_record', to='data_management.animalprofile'),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='date_weighted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='livestock',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='breed', to='data_management.livestock'),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='dam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dam_of', to='data_management.animalprofile'),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='sire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sire_of', to='data_management.animalprofile'),
        ),
    ]
