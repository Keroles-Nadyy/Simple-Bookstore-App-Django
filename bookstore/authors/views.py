from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from authors.forms import AuthorForm, AuthorModelForm
from authors.models import Author

# Create your views here.

def authors_main(request):
    authors = Author.get_all_authors()
    return render(request, 'authors/all_authors.html', context={"authors":authors})

@login_required(login_url='accounts/login')
def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            new_author = Author(name=form.cleaned_data['name'],
                                image=form.cleaned_data['image'],
                                DOB=form.cleaned_data['DOB']
                            )
            new_author.save()
            return HttpResponse("Track added successfully")
    return render(request, 'authors/add_author.html', context={'form': form})


def show_author(request, id):
    author = Author.get_author(id)
    return render(request, 'authors/show_author.html', context={"author":author})

@login_required(login_url='accounts/login')
def create_author_MF(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            return redirect(author.show_author_url)
    return render(request, 'authors/add_author.html', context={'form': form})


@login_required(login_url='accounts/login')
def edit_author_info_from_DB(request, id):
    selected_author = Author.get_author(id)
    form = AuthorModelForm(instance=selected_author)
    if request.method == 'POST':
        form  = AuthorModelForm(request.POST, request.FILES, instance=selected_author)
        if form.is_valid():
            form.save()
            return redirect(selected_author.show_author_url)
    return render(request, 'authors/edit_author.html', context={"form": form})


@login_required(login_url='accounts/login')
def delete_author_from_DB(request, id):
    deleted_author = Author.objects.get(id=id)
    deleted_author.delete()
    url = reverse('authors.landing')
    return redirect(url)