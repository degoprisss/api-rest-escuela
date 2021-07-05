# Create your views here.
from rest_framework.viewsets import ModelViewSet

from apprentices.models import Apprentices
from apprentices.serializers import SerializerStudents
from teachers.models import Teachers
from teachers.serializers import SerializerTeachers


class TeachersViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = SerializerTeachers

    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            if key in ['page', 'limit', 'offset']:
                continue
            data[key] = value
        return self.queryset.filter(**data)
