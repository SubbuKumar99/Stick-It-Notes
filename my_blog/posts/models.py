from django.db import models

# Create your models here.



class PostStorage(models.Model):#
    colour_choices = ((1,'Yellow'),(2,'Green'),(3,'Purple'),(4,'Blue'),(5,'Orange'))

    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    colour = models.CharField(max_length=6,choices=colour_choices,default='Yellow')
    created_at = models.DateTimeField(auto_now_add=True)
