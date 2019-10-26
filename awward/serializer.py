from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ('image_path', 'project_title', 'description','link ')