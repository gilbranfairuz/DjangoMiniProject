from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255, blank=False)
	body = models.TextField(blank=True)
	alamat = models.CharField(max_length=255, blank=True)
	email = models.EmailField(default='nama@web.com')
	waktu_posting = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.title)