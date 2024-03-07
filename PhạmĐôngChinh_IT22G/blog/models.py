from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    categoryBlog = models.CharField(max_length=32)
    content = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images', null=True)
    audio = models.FileField(upload_to='media/audios', null=True)
    imageAuthor = models.ImageField(upload_to='media/images', null=True)

    def __str__(self):
        return self.title

class CategoryBlog(models.Model):
    categoryBlog = models.CharField(max_length=32)

    def __str__(self):
        return self.categoryBlog