from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    reading_time = models.IntegerField()
    description = models.TextField()

    def __str__(self): 
        return self.title
