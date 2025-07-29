from django.db import models

# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
