from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=250,blank=False,null=False)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

