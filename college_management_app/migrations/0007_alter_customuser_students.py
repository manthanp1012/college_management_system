# Generated by Django 4.2.7 on 2023-11-20 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0006_customuser_students_alter_students_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='students',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to='college_management_app.students'),
        ),
    ]
