# Generated by Django 4.1.1 on 2022-09-16 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='seat',
            new_name='all_seat',
        ),
    ]