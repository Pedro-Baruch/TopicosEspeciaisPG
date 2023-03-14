from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=80, null=False, blank=True)
    texto = models.CharField(max_length=300, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now=True)
    gostei = models.PositiveSmallIntegerField(default=0)