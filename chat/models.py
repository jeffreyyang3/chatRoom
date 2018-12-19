from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    isInstructor = forms.BooleanField()
    
    userID = models.CharField(max_length = 15)


class ChatMessage(models.Model):
    """
    Model to represent a chat message
    """

    #Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String to represent the message
        """

        return self.message