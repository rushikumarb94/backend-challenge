from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    """
    Represents a label that can be associated with tasks.
    """
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labels')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Order labels by name

class Task(models.Model):
    """
    Represents a task in the task management system.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    labels = models.ManyToManyField(Label, related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']  # Order tasks by most recently updated