# Generated by Django 4.1.7 on 2023-03-25 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backplat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachersubject',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='teachersubject',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
