import io

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import TeacherSubject, Group, Subject


#Convert json format into python format or vice versa

# class GroupModel:
#     def __init__(self, name, teacher, subject):
#         self.name = name
#         self.teacher = teacher
#         self.subject = subject


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', 'teacher', 'subject']

    # group_name = serializers.CharField(max_length=255)
    # teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    def to_representation(self, instance):  # allows change representation of data only! for GET request
        print(instance)
        data = super().to_representation(instance)
        # print(type(data))
        return data

    def validate(self, data):  # allows to validate the incoming data. if write validate_fieldname - such method validates this field.
        teacher_id = data["teacher"].id
        subject_id = data["subject"].id

        try:
            TeacherSubject.objects.get(teacher=teacher_id, subject=subject_id)

        except ObjectDoesNotExist:
            teacher = User.objects.get(id=teacher_id)
            return Response(data={'error': f'{teacher.first_name} {teacher.last_name} doesn\'t teach this subject'},
                            status=400)

        return data

    def create(self, validated_data):
        print(validated_data)
        return Group.objects.create(**validated_data)





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
