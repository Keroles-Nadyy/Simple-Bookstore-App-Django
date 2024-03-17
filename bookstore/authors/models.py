from django.db import models
from django.shortcuts import reverse, get_object_or_404


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/images/', null=True)
    DOB = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_author_url(self):
        url = reverse("author.profile", args=[self.id])
        return url
    
    @classmethod
    def get_all_authors(cls):
        return cls.objects.all()
    
    @classmethod
    def get_author(cls, id):
        # return cls.objects.get(id=id)
        return get_object_or_404(cls, id=id)
    

