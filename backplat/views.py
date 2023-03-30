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
        # print(request.data["teacher"])
        lst = Group.objects.filter(teacher=request.data["teacher"]).order_by("group_name")

        return Response({'groups': GroupSerializer(lst, many=True).data})
    # def get(self, request):
    #     lst = Group.objects.all().values()
    #
    #     return Response({'group': list(lst)})

    def post(self, request):
        serializer = GroupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'post': serializer.data})


def index(request):
    return HttpResponse("Hi")
