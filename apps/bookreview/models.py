from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20, null=True)
	last_name = models.TextField(blank=False, max_length=20,null=True)
	email = models.TextField(blank=False, max_length=20,null=True)
	description = models.TextField(blank=False, max_length=500,null=True)
	password = models.TextField(blank=False, max_length=20,null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'user'

class Book(models.Model):
	title = models.TextField(blank=False, max_length=20, null=True)
	author = models.TextField(blank=False, max_length=20,null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'book'

class Review(models.Model):
	review = models.TextField(blank=False, max_length=250, null=True)
	user = models.ForeignKey(User, related_name="user")
	book = models.ForeignKey(Book, related_name="book")
	rating = models.IntegerField(blank=False, null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'review'




