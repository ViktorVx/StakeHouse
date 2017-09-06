from django.db import models

# Create your models here.
class News(models.Model):
	name = models.CharField(max_length=64)
	header = models.CharField(max_length=256)
	full_description = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.header