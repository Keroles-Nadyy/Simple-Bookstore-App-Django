from django.urls import path, include
from accounts.views import register, custom_logout




urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', register, name='account.create'),
    path('logout', custom_logout, name='logout'),
]