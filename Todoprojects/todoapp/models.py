from django.db import models

# Create your models here.

class Todo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    start_time=models.TimeField(auto_now_add=True)
    end_time=models.TimeField(auto_now_add=True)
    content=models.TextField()
    is_done=models.BooleanField(default=False)

    class Meta:
        ordering=['created']
