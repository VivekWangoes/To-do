from .models import *
from rest_framework import serializers


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTaskModel
        fields = '__all__'
