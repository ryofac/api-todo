from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "description", "created_at", "end_at", "is_active"]
        read_only_fields = ["id"]
