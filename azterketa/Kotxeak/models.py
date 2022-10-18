from django.db import models

class Kotxea(models.Model):
  marca = models.CharField(max_length=255)
  modelo = models.CharField(max_length=255)
  matricula = models.CharField(max_length=255)
  precioHora = models.FloatField()
  alokatzeData = models.DateField()

