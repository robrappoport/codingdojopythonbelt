# Generated by Django 2.0 on 2019-06-24 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beltExam_app', '0004_trips_reason_for_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='trips',
            name='joined_by',
        ),
        migrations.DeleteModel(
            name='Trips',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
