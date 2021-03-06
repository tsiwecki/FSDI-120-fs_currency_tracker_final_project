# Generated by Django 3.2.6 on 2021-09-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot_log', '0008_alter_flightdetail_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetail',
            name='day_landings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdetail',
            name='holds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdetail',
            name='instrument_appchs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdetail',
            name='night_landings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
