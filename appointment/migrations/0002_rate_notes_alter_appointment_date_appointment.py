# Generated by Django 4.1 on 2022-08-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_appointment',
            field=models.DateField(blank=True, null=True),
        ),
    ]