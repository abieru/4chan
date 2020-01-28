from django.db import models
from django.utils.timezone import now
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name="Nombre")
	created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edición")
	

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = "Categorias"
		ordering = ["-created"]

	def __str__(self):
		return self.name   

class Post(models.Model):
	name = models.CharField(max_length=100, verbose_name="Name", null=True, blank=True)
	categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
	image = models.ImageField(verbose_name="Imagen", upload_to="thread", null=True, blank=True)
	content = models.TextField( verbose_name="contenido")
	created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edición", null=True, blank= True) 
	published = models.DateTimeField(verbose_name="Fecha de publicación", default=now) 
