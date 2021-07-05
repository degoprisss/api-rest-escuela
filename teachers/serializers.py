from rest_framework.serializers import ModelSerializer

from apprentices.models import Apprentices
from classes.models import Classes
from teachers.models import Teachers


class SerializerTeachers(ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'