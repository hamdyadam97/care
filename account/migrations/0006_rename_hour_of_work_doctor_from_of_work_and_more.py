# Generated by Django 4.1 on 2022-08-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_doctor_day1_of_work_alter_doctor_day2_of_work_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='hour_of_work',
            new_name='from_of_work',
        ),
        migrations.AddField(
            model_name='doctor',
            name='to_of_work',
            field=models.IntegerField(blank=True, null=True, verbose_name='to_of_work'),
        ),
    ]
