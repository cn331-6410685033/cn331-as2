# Generated by Django 4.1.1 on 2022-09-16 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_student_courses_course_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='all_seat',
            new_name='max_seat',
        ),
    ]
