# Generated by Django 4.1.1 on 2022-09-16 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
    ]