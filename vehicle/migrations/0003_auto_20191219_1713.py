# Generated by Django 2.2.6 on 2019-12-19 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20191219_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='status',
            new_name='blacklisted',
        ),
    ]