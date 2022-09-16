# Generated by Django 4.1.1 on 2022-09-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0005_course_quota_course_semester_course_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(blank=True, related_name='student_course', to='courses.course')),
            ],
        ),
    ]
