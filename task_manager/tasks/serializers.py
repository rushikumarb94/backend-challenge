from rest_framework import serializers
from .models import Task, Label

class LabelSerializer(serializers.ModelSerializer):
    """
    Serializer for the Label model.
    """
    class Meta:
        model = Label
        fields = ['id', 'name', 'owner']
        read_only_fields = ['owner']

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'owner', 'labels', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']