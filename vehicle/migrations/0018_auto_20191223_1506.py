# Generated by Django 2.2.6 on 2019-12-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0017_auto_20191223_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[('Hybrid', 'Hybrid'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='gear_type',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=10),
        ),
    ]
