from django.contrib import admin
from backplat.models import Subject, TeacherSubject, Group, StudentGroup, Assignment, Mark


admin.site.register(Subject)
admin.site.register(TeacherSubject)
admin.site.register(Group)
admin.site.register(StudentGroup)
admin.site.register(Assignment)
admin.site.register(Mark)