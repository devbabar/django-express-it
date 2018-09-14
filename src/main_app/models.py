from django.db import models
from django.contrib.auth.models import User



class ExpressIt(models.Model):
	user=models.ForeignKey(User)
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=200)
	location=models.CharField(max_length=100)
	image=models.ImageField(upload_to='express_it_images',default='media/default.png')
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


	def __unicode__(self):
		return self.name
