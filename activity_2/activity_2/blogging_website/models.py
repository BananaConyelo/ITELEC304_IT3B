from django.db import models

# Create your models here.

class Author(models.Model):
    name_author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year_publised = models.IntegerField()

    def __str__(self):
        return self.name_author
    

class Category(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.author.name_author}'Category"
    
class Post(models.Model):
    recommendation = models.CharField(max_length=100)
    opinion = models.CharField(max_length=100)
    rate = models.IntegerField()
    def __str__(self):
        return self.recommendation

class Tag(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    comment = models.CharField()
    is_active = models.BooleanField(default=True)



