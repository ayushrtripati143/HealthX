# Generated by Django 4.0.4 on 2023-03-19 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_appointment_rest_data_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment_rest_data',
            old_name='Time',
            new_name='time',
        ),
    ]
