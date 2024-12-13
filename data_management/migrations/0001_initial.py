# Generated by Django 4.2.16 on 2024-12-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('weight', models.FloatField()),
                ('health_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MilkProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField()),
                ('quantity_litres', models.FloatField()),
                ('livestock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milk_records', to='data_management.livestock')),
            ],
        ),
    ]