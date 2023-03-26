from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import TeacherSubject, Group, Subject
from .serializers import GroupSerializer


# class PlatformAPIView(generics.ListAPIView):
#     queryset = TeacherSubject.objects.all()
#     serializer_class = TeacherSerializer
#
#
# class DashboardAPIView(generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# training class
class DashboardAPIView(APIView):
    def get(self, request):
        lst = Group.objects.all()

        return Response({'group': GroupSerializer(lst, many=True).data})
    # def get(self, request):
    #     lst = Group.objects.all().values()
    #
    #     return Response({'group': list(lst)})

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        print(request.data)
        print(serializer.is_valid())
        serializer.is_valid(raise_exception=True)
        teacher_id = request.data['teacher_id']
        subject_id = request.data['subject_id']

        try:
            TeacherSubject.objects.get(teacher=teacher_id, subject=subject_id)

        except ObjectDoesNotExist:
            teacher = User.objects.get(id=teacher_id)
            return Response(data={'error': f'{teacher.first_name} {teacher.last_name} doesn\'t teach this subject'},
                            status=400)

        post_new = Group.objects.create(
            group_name=request.data['group_name'],
            teacher=User.objects.get(id=teacher_id),
            subject=Subject.objects.get(id=subject_id)
        )

        # return Response({'post': model_to_dict(post_new)})

        return Response({'post': GroupSerializer(post_new).data})


def index(request):
    return HttpResponse("Hi")
