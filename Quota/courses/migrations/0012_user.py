# Generated by Django 4.1.1 on 2022-09-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_rename_student_course_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(blank=True, related_name='student', to='courses.course')),
            ],
        ),
    ]
