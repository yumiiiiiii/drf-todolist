from rest_framework import serializers
from todoapp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id', 'start_time', 'end_time', 'content', 'is_done']