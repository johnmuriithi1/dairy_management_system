# data_management/migrations/0006_remove_animalprofile_livestock_and_more.py
from django.db import migrations, models
import django.db.models.deletion

def set_default_livestock_type(apps, schema_editor):
    AnimalProfile = apps.get_model('data_management', 'AnimalProfile')
    LiveStockType = apps.get_model('data_management', 'LiveStockType')

    # Create a default LiveStockType if none exists
    if not LiveStockType.objects.exists():
        default_type = LiveStockType.objects.create(name="Unknown")  # Or a more descriptive default
    else:
        default_type = LiveStockType.objects.first()

    # Update existing AnimalProfile records
    AnimalProfile.objects.update(livestock_type=default_type)

class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0005_remove_animalprofile_breed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalprofile',
            name='livestock',
        ),
        migrations.AddField(
            model_name='animalprofile',
            name='livestock_type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='data_management.livestocktype',
                default=1 # Temporary default, will be overwritten
            ),
            preserve_default=False, # Crucial: Remove the default after the data migration
        ),
        migrations.RunPython(set_default_livestock_type),
    ]