from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    completed = filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['title', 'completed']

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LabelFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    completed = filters.BooleanFilter()

    class Meta:
        model = Label
        fields = ['name']

class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Label.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LabelFilter

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)