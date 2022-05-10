from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FAQ(models.Model):
    title = models.TextField()
    category = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Inquiry(models.Model):
    Inquiry_title = models.TextField()
    Inquiry_category = models.TextField() 
    Inquiry_email = models.TextField()
    Inquiry_number = models.TextField()
    Inquiry_updated_at = models.DateTimeField(auto_now=True)
    Inquiry_writer =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Answer(models.Model):
    answer = models.TextField(verbose_name="질문")
