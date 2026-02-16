from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post1(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    #INSTANCE METHOD
    def show_title(self):
        return f'{self.author} wrote the {self.title} with the category of {self.category}'
    
    #SPECIAL METHOD
    def __str__(self):
        return self.title
    
    #CLASS METHOD
    @classmethod
    def total_post(cls):
        return cls.objects.count()