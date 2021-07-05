from rest_framework.serializers import ModelSerializer

from apprentices.models import Apprentices
from classes.models import Classes


class SerializerClasses(ModelSerializer):

    class Meta:
        model = Classes
        fields = '__all__'