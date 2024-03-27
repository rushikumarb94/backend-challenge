from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Task model.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LabelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Label model.
    """
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Label.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)