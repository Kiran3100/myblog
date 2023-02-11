from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class PostModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_date",)

