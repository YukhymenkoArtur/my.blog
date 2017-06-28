from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	content = models.TextField()
	link_to_image = models.CharField(max_length=25000)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)
	create = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		verbose_name="Стаття"
		verbose_name_plural="Статті"
		ordering=["-create"]

	def __str__ (self):
		return self.title




#new_today
# class Comment(models.Model):
# 	post = models.ForeignKey('blog.Post', related_name='comments')
# 	author = models.CharField(max_length=200)
# 	text = models.TextField()
# 	created_date = models.DateTimeField(default=timezone.now)
# 	approved_comment = models.BooleanField(default=False)

# 	def approve(self):
# 		self.approved_comment = True
# 		self.save()

# 	def __str__(self):
# 		return self.text
