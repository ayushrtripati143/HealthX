# Generated by Django 4.0.4 on 2023-03-03 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_add_hospital_data_oxygen'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_appointment',
            name='mail',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
