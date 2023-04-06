from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import TeacherSubject, Group, Subject, Assignment, Mark, StudentGroup
from .permissions import IsOwnerOrAdminUser
from .serializers import GroupSerializer, AssignmentSerializer, SubjectSerializer


class SubjectListAPI(generics.ListAPIView):
    """
    Get all teachers subjects
    """
    queryset = TeacherSubject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        queryset = get_list_or_404(klass=self.filter_queryset(self.get_queryset()), teacher=request.user.id)
        serializer = self.get_serializer(queryset, many=True)

        subjects_list = [
            {
                "id": data["subject"],
                "name": Subject.objects.get(pk=data["subject"]).subject_name
            }
            for data in serializer.data
        ]

        subjects_dict = {
            "subjects": subjects_list
        }

        return Response(subjects_dict)


class GroupListAPI(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(teacher=request.user.id)
        serializer = self.get_serializer(queryset, many=True)

        return Response({"groups": serializer.data})

    def post(self, request, *args, **kwargs):

        get_object_or_404(klass=TeacherSubject,
                          teacher=request.data["teacher"],
                          subject=request.data["subject"])

        return self.create(request, *args, **kwargs)


class GroupChangeAPI(generics.UpdateAPIView,
                     generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdminUser )


class AssignmentListAPI(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        queryset = get_list_or_404(klass=self.filter_queryset(self.get_queryset()), group=kwargs["pk"])

        group_teacher = queryset[0].group.teacher
        self.check_permission(group_teacher, request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"assignments": serializer.data})

    def post(self, request, *args, **kwargs):
        group_teacher = get_object_or_404(klass=Group, id=kwargs["pk"]).teacher

        self.check_permission(group_teacher, request.user)

        request.data["group"] = kwargs["pk"]
        return self.create(request, *args, **kwargs)
    def check_permission(self, teacher, user):
        if teacher != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to get this info.")



# training class
class DashboardAPIView(APIView):
    def get(self, request):
        # print(request.data["teacher"])
        lst = Group.objects.filter(teacher=request.data["teacher"]).order_by("group_name")

        return Response({"groups": GroupSerializer(lst, many=True).data})


    def post(self, request):
        serializer = GroupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
