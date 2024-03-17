from django import forms
from authors.models import Author


class AuthorForm(forms.Form):
    name = forms.CharField(label="name",max_length=100)
    image = forms.ImageField(label="image")
    DOB = forms.DateTimeField(label="Date of birth")


    def clean_name(self):
        name= self.cleaned_data['name']
        
        if len(name) < 3:
            raise forms.ValidationError("Author name does not valid")
        elif Author.objects.filter(name=name).exists():
            raise forms.ValidationError("Author is already exist")
        return name
    
class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'image', 'DOB']

    def clean_name(self):
        name= self.cleaned_data['name']
        
        if len(name) < 3:
            raise forms.ValidationError("Author name does not valid")
        elif Author.objects.filter(name=name).exists():
            raise forms.ValidationError("Author is already exist")
        return name