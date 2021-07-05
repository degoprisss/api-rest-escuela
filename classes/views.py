from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apprentices.models import Apprentices
from apprentices.serializers import SerializerStudents
from classes.models import Classes
from classes.serializers import SerializerClasses


class ClassesViewSet(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = SerializerClasses

    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            if key in ['page', 'limit', 'offset']:
                continue
            data[key] = value
        return self.queryset.filter(**data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def students(self, request, pk):
        classStudents = self.get_object()
        if request.method == 'GET':
            students = classStudents.students.all()

            page = self.paginate_queryset(students)
            if page:
                serializer = SerializerStudents(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(students, many=True)

            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            listStudent = request.data['students']

            for value in listStudent:
                students = Apprentices.objects.get(id=value)
                serializers = SerializerClasses(classStudents)
                classStudents.students.add(students)
                classStudents.save()

                return Response(status=status.HTTP_200_OK, data=serializers.data)
