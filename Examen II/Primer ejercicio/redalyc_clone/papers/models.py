from django.db import models

# Create your models here.

class trabajos(models.Model):
	titulo= models.CharField(max_length=40)
	autor=models.CharField(max_length=40)
	categorias=(('CC','Ciencias Computacionales'),
		('CT','Ciencias de la Tierra'),('CN','Ciencias Naturales'),
		('CS','Ciencias Sociales'),('CM','Ciencias Medicas'))
	categoria=models.CharField(max_length=2, choices=categorias)
	docfile=models.FileField(upload_to='archivos/%Y/%m/%d')


	def __str__(self):
		return self.titulo