from rest_framework.serializers import ModelSerializer
from .models import CSVObject


class CSVObjectSerializer(ModelSerializer):
    class Meta:
        model = CSVObject
        fields = '__all__'
