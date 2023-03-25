from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)


class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    student = models.ForeignKey(User, on_delete=models.PROTECT)


class Assignment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    assign_deadline = models.DateTimeField()
    assign_text = models.CharField(max_length=1024, null=True)


class Mark(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    mark = models.IntegerField(blank=True)
