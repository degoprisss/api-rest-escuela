from rest_framework.serializers import ModelSerializer

from apprentices.models import Apprentices


class SerializerStudents(ModelSerializer):

    class Meta:
        model = Apprentices
        fields = '__all__'
