from django.db import models


class Subject(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    subject_name = models.CharField(max_length=200, db_column='subject_name')


class TeacherSubject(models.Model):
    teacher_id = models.ForeignKey(to_field='id')
    subject_id = models.ForeignKey(Subject, on_delete=, to_field='id')
