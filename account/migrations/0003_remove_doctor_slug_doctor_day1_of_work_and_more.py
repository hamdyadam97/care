# Generated by Django 4.1 on 2022-08-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_profile_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='slug',
        ),
        migrations.AddField(
            model_name='doctor',
            name='day1_of_work',
            field=models.IntegerField(blank=True, null=True, verbose_name='day1_of_work'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='day2_of_work',
            field=models.IntegerField(blank=True, null=True, verbose_name='day2_of_work'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='day3_of_work',
            field=models.IntegerField(blank=True, null=True, verbose_name='day3_of_work'),
        ),
    ]
