import io

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import TeacherSubject, Group, Subject


#Convert json format into python format or vice versa

# class GroupModel:
#     def __init__(self, name, teacher, subject):
#         self.name = name
#         self.teacher = teacher
#         self.subject = subject


class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=255)
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    def validate_teacher(self, value):
        if value is None:
            raise serializers.ValidationError("Teacher field is required.")
        return value

    def validate_subject(self, value):
        if value is None:
            raise serializers.ValidationError("Subject field is required.")
        return value

# def encode():
#     model = GroupModel('2A', 'Garfield', 'Pie')
#     model_sr = GroupSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"2A","teacher":"Garfield","subject":"Pie"}')
#     data = JSONParser().parse(stream)
#     serializer = GroupSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



# class TeacherSerializer(serializers.Serializer):
#     class Meta:
#         model = TeacherSubject
#         fields = ('id', 'teacher_id', 'subject_id')
#
# class GroupSerializer(serializers.Serializer):
#     class Meta:
#         model = Group
#         fields = ('group_name', 'subject')
