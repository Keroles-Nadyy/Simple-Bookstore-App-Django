from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from accounts.forms import AccountForm
from django.contrib.auth import logout


def profile(request):
    url = reverse('books.landing')
    return redirect(url)

def custom_logout(request):
    logout(request)
    url = reverse('books.landing')
    return redirect(url)

def register(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'accounts/create_account.html', context={'form':form})