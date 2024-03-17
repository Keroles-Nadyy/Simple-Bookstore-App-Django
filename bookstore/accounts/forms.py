from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ('first_name', 'last_name', 'email', 'username', 'password')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    
    def save(self, commit=True):
        self.instance.password= make_password(password=self.instance.password)
        super().save()
        return self.instance
