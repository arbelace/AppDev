from django.db import models




class TodoItem(models.Model):
    title = models.CharField(max_Lenght=200)
    completed = models.BoonleanField(default=False)