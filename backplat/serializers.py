import io

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import TeacherSubject, Group, Subject, Assignment


#Convert json format into python format or vice versa

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = ["subject"]


    # def to_representation(self, instance):  # allows change representation of data only! for GET request
    #     # print(instance)
    #     data = super().to_representation(instance)
    #     # print(type(data))
    #     return data
    #
    # def validate(self, data):  # allows to validate the incoming data. if write validate_fieldname - such method validates this field.
    #     teacher_id = data["teacher"].id
    #     subject_id = data["subject"].id
    #     try:
    #         TeacherSubject.objects.get(teacher=teacher_id, subject=subject_id)
    #
    #     except ObjectDoesNotExist:
    #         teacher = User.objects.get(id=teacher_id)
    #
    #         return Response(data={'error': f'{teacher.first_name} {teacher.last_name} doesn\'t teach this subject'}, status=400)
    #     # print(type(data))
    #     return data

