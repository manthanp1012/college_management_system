# Generated by Django 4.2.7 on 2023-11-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0013_alter_subjects_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='admin',
        ),
    ]
