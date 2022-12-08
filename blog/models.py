from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    STATUS = {
        ('recluter','Recluter'),
        ('publicado','Publicado')
    }
    titulo = models.CharField(max_length=250)
    slug =   models.SlugField(max_length=250)#https://site.com/noticias/campeonato-2022/01/02/2022 
    autor = models.ForeignKey(User,
                              on_delete = models.CASCADE)
    contenido = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='recluter')  

    class Meta:
        ordering = ('publicado',)

    def __str__(self):
        return self.titulo