from django import forms
from books.models import Book


class BookForm(forms.Form):
    name = forms.CharField(label="name",max_length=100)
    desc = forms.CharField(label="desc",max_length=1024)
    image = forms.ImageField(label="image")
    author = forms.CharField(label="author", max_length=255)
    pages = forms.IntegerField(label="pages")
    price = forms.FloatField(label="price")


    def clean_name(self):
        name= self.cleaned_data['name']
        if Book.objects.filter(name=name).exists() and name != self.instance.name: 
            raise forms.ValidationError("Book Name is already exist")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 30:
            raise forms.ValidationError("Price must be at leasr 20 L.E")
        return price
    

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"        

    def clean_name(self):
        name= self.cleaned_data['name']
        if Book.objects.filter(name=name).exists()  and name != self.instance.name:
            raise forms.ValidationError("Book Name is already exist")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 30:
            raise forms.ValidationError("Price must be at leasr 20 L.E")
        return price