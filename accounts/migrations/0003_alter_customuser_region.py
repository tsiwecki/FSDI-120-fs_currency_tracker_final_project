# Generated by Django 3.2.6 on 2021-09-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_user_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.CharField(choices=[('1', '1 - Northern'), ('2', '2 - Rocky Mountain'), ('3', '3 - Southwestern'), ('4', '4 - Intermountain'), ('5', '5 - Pacific Southwest'), ('6', '6 - Pacific Northwest'), ('8', '8 - Southern'), ('9', '9 - Eastern'), ('10', '10 - Alaska'), ('WO', 'Washington Office')], default='WO', max_length=4),
        ),
    ]
