# Generated by Django 4.2.16 on 2025-01-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0010_animalprofile_document_upload_animalprofile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
