# Generated by Django 2.2.6 on 2019-12-20 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='from_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='to_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='from_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='to_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]