# Generated by Django 4.2.7 on 2023-11-20 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0007_alter_customuser_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='students',
        ),
        migrations.AlterField(
            model_name='students',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
