# Generated by Django 2.0 on 2019-06-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltExam_app', '0003_auto_20190624_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='reason_for_trip',
            field=models.CharField(default='No Listed Reason For Trip', max_length=500),
            preserve_default=False,
        ),
    ]
