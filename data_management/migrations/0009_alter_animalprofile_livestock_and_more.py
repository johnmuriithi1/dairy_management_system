# Generated by Django 4.2.16 on 2025-01-06 06:43

from django.db import migrations, models
import django.db.models.deletion

def set_default_livestock(apps, schema_editor):
    AnimalProfile = apps.get_model('data_management', 'AnimalProfile')
    LiveStock = apps.get_model('data_management', 'LiveStock')
    LiveStockType = apps.get_model('data_management', 'LiveStockType')
    try:
        #Try to get an existing livestock type
        livestock_type = LiveStockType.objects.first()
        if livestock_type:
            #Try to get an existing livestock with the livestock type
            livestock = LiveStock.objects.filter(livestock_type=livestock_type).first()
            if livestock:
                default_livestock = livestock
            else:
                #Create default livestock if none exists
                default_livestock = LiveStock.objects.create(farmer_id=1, name="Default Livestock",)
                default_livestock.livestock_type.add(livestock_type)
        else:
            #Create a default livestock type if none exists
            livestock_type = LiveStockType.objects.create(name="Default Type")
            #Create default livestock if none exists
            default_livestock = LiveStock.objects.create(farmer_id=1, name="Default Livestock")
            default_livestock.livestock_type.add(livestock_type)
    except Exception as e:
        print(f"Error creating default livestock: {e}")
        return

    AnimalProfile.objects.filter(livestock__isnull=True).update(livestock=default_livestock)


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0008_remove_animalprofile_livestock_type_and_more'),
    ]

    operations = [
        migrations.RunPython(set_default_livestock),  # Run the data migration FIRST
        migrations.AlterField(
            model_name='animalprofile',
            name='livestock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='data_management.livestock'),
        ),
        migrations.RemoveField(
            model_name='livestock',
            name='livestock_type',
        ),
        migrations.AddField(
            model_name='livestock',
            name='livestock_type',
            field=models.ManyToManyField(related_name='livestock', to='data_management.livestocktype'),
        ),
    ]