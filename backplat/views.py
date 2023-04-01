from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import TeacherSubject, Group, Subject, Assignment
from .serializers import GroupSerializer, AssignmentSerializer, SubjectSerializer


class SubjectListAPI(generics.ListAPIView):
    queryset = TeacherSubject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(teacher=request.user.id)
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
        # group_queryset = self.filter_queryset(self.get_queryset()).filter(teacher=request.user.id)
        #
        # # Get the subjects that belong to the current user
        # teacher_subjects = TeacherSubject.objects.filter(teacher=request.user)
        #
        # # Create a dictionary mapping subject IDs to subject names
        # subject_dict = {subject.id: subject.subject.subject_name for subject in teacher_subjects}
        # print(subject_dict)
        # # Serialize the groups and add the subject information to each group
        # serialized_groups = []
        # for group in group_queryset:
        #     serialized_group = self.get_serializer(group).data
        #     print(serialized_group)
        #     serialized_group['subject'] = [subject_dict[subject.id] for subject in group.objects.all()]
        #     serialized_groups.append(serialized_group)
        #
        # # Return the serialized data in a response
        # return Response({"groups": serialized_groups})
        return Response({"groups": serializer.data})

class GroupAPI(generics.UpdateAPIView,
               generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )


class AssignmentListAPI(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializers = AssignmentSerializer
    permission_classes = (IsAuthenticated, )




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
