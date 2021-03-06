from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from apprentices.models import Apprentices
from apprentices.serializers import SerializerStudents
from apprentices.tasks import student_email


class StudentsViewSet(ModelViewSet):
    queryset = Apprentices.objects.all()
    serializer_class = SerializerStudents

    #Filter
    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            if key in ['page', 'limit', 'offset']:
                continue
            data[key] = value
        return self.queryset.filter(**data)

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer_class()
        serialized = serializers(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        student_email.apply_async(args=['degoprisss@gmail.com'])


        return Response(status=status.HTTP_200_OK, data=serialized.data)