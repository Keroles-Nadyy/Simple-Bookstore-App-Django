from django.db import models
from authors.models import Author
from django.shortcuts import reverse, get_object_or_404


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(max_length=1024, null=True)
    image = models.ImageField(upload_to='books/images/', null=True)
    # author = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages = models.IntegerField(null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def edit_url(self):
        url = reverse("book.edit", args=[self.id])
        return url
    
    @property
    def show_url(self):
        url = reverse("book.profile", args=[self.id])
        return url
    
    @classmethod
    def create_object(cls, name, desc, image, author, pages, price):
        try:
            Book = cls(name=name, desc=desc, image=image, author=author, pages=pages, price=price)
            Book.save()
        except Exception as e :
            return False
        else:
            return Book
        
    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)