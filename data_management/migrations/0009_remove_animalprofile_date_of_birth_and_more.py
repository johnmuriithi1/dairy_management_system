# Generated by Django 4.2.16 on 2025-01-09 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0008_remove_animalprofile_livestock_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='date_weighted',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='animalprofile',
            name='uploaded_document',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='breeding_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='dam',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='expected_birth_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='offspring',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='sire',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='cause_of_death',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='disposal_method',
        ),
        migrations.RemoveField(
            model_name='deathrecord',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='event',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='event',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='name',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='price',
        ),
        migrations.RemoveField(
            model_name='healthrecord',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='healthrecord',
            name='description',
        ),
        migrations.RemoveField(
            model_name='livestock',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='milkproduction',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='milkproduction',
            name='production_date',
        ),
        migrations.RemoveField(
            model_name='milkproduction',
            name='quantity_litres',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='administered_by',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='batch_number',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='date_given',
        ),
        migrations.RemoveField(
            model_name='vaccinationrecord',
            name='next_vaccination_date',
        ),
        migrations.AddField(
            model_name='animalprofile',
            name='birth_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Birth Weight (kg)'),
        ),
        migrations.AddField(
            model_name='animalprofile',
            name='health_status',
            field=models.CharField(default='Healthy', max_length=100, verbose_name='Health Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animalprofile',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='expected_due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expected Due Date'),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='breeding_records', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='mating_date',
            field=models.DateField(default='2025-01-01', verbose_name='Mating Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='outcome',
            field=models.CharField(choices=[('success', 'Success'), ('failure', 'Failure'), ('pending', 'Pending')], default='pending', max_length=7, verbose_name='Outcome'),
        ),
        migrations.AddField(
            model_name='deathrecord',
            name='cause',
            field=models.CharField(default='Unknown', max_length=255, verbose_name='Cause of Death'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathrecord',
            name='date',
            field=models.DateField(default='2025-01-01', verbose_name='Date of Death'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathrecord',
            name='livestock',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='death_record', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='date',
            field=models.DateField(default='2025-01-01', verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='feed_type',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Feed Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='issue',
            field=models.CharField(default='None', max_length=255, verbose_name='Health Issue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='health_records', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='veterinarian',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Veterinarian'),
        ),
        migrations.AddField(
            model_name='livestock',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='livestock',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='None', max_length=6, verbose_name='Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestock',
            name='unique_id',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='Unique Identifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livestocktype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='date',
            field=models.DateField(default='2025-01-01', verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='milk_productions', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milkproduction',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='Quantity (liters)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccinationrecord',
            name='date_administered',
            field=models.DateField(default='2025-01-01', verbose_name='Date Administered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccinationrecord',
            name='livestock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='data_management.livestock', verbose_name='Livestock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccinationrecord',
            name='next_due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Next Due Date'),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='livestock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='data_management.livestock', verbose_name='Livestock'),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Weight (kg)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(max_length=100, verbose_name='Event Type'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Quantity (kg)'),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='treatment',
            field=models.TextField(verbose_name='Treatment Details'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='livestock_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livestocks', to='data_management.livestocktype', verbose_name='Livestock Type'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Livestock Name'),
        ),
        migrations.AlterField(
            model_name='livestocktype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Livestock Type'),
        ),
        migrations.AlterField(
            model_name='vaccinationrecord',
            name='vaccine_name',
            field=models.CharField(max_length=100, verbose_name='Vaccine Name'),
        ),
    ]
