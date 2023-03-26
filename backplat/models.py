from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        full_name = (self.teacher.first_name + '  ' + self.teacher.last_name + ' - ' + self.subject.subject_name)
        return full_name


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        name = (self.group_name + ' - ' + self.subject.subject_name)
        return name

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
