# Generated by Django 2.2.6 on 2019-12-19 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]