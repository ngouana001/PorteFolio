from django.db import models

class Projet(models.Model):
     titre=models.CharField(max_length=50)
     description=models.TextField()
     image=models.CharField(max_length=2000)