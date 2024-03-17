from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from books.forms import BookForm, BookModelForm
from django.contrib.auth.decorators import login_required

from books.models import Book

# Create your views here.
    # Create a list of books
# book_list = [
#     {"id":1, "name":"The Monk Who Sold His Ferrari: A Fable About Fulfilling Your Dreams and Reaching Your Destiny", "desc": "The Monk Who Sold His Ferrari: A Fable About Fulfilling Your Dreams and Reaching Your Destiny by motivational speaker and author Robin Sharma is an inspiring tale that provides a step-by-step approach to living with greater courage, balance, abundance and joy. ", "image":"book1.jpg", "author":"   ", "price":300},
#     {"id":2, "name":"Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones", "desc": "No matter your goals, Atomic Habits offers a proven framework for improving - every day. James Clear, one of the world's leading experts on habit formation, reveals practical strategies that will teach you exactly how to form good habits, break bad ones, and master the tiny behaviors that lead to remarkable results.", "image":"book2.jpg", "author":"James Clear", "price":630},
#     {"id":3, "name":"Thinking, Fast and Slow", "desc":"Thinking, Fast and Slow, Kahneman at last offers his own, first book for the general public. It is a lucid and enlightening summary of his life's work. It will change the way you think about thinking. " , "image":"book3.jpg", "author":"Daniel Kahneman", "price":350},
#     {"id":4, "name":"48 Laws of Power", "desc":"This bold volume outlines the laws of power in their unvarnished essence, synthesizing the philosophies of Machiavelli, Sun Tzu, Carl von Clausewitz, and other infamous strategists. The 48 Laws of Power will fascinate any listener interested in gaining, observing, or defending against ultimate control." , "image":"book4.jpg", "author":"Robert Greene", "price":480},
#     {"id":5, "name":"Who moved my cheese?", "desc":"It is the amusing and enlightening story of four characters who live in a maze and look for cheese to nourish them and make them happy. Cheese is a metaphor for what you want to have in life, for example a good job, a loving relationship, money or possessions, health or spiritual peace of mind. The maze is where you look for what you want, perhaps the organisation you work in, or the family or community you live in. ", "image":"book5.jpg", "author":"Dr Spencer Johnson", "price":320},
#     {"id":6, "name":"Book6", "image":"pic1.png", "author":"author6", "price":100},
# ]

# def index(request):
#     return HttpResponse(book_list)

# def all_books(request):
#     return render(request, "books/all_books.html", context={"books": book_list})

# def get_book(request, book_id):
#     for book in book_list:
#         if book["id"] == book_id:
#             # return HttpResponse(book.values())
#             print(book)
#             print(list(book))
#             # return render(request, 'books/bookProfile.html', context={"bookInfo":list(book)[0]})
#             return render(request, 'books/bookProfile.html', context={"bookInfo":book})
#     return HttpResponse("Book does not exist")
# def create_new_book(request):
#     if request.method == 'POST':
#         new_book = Book()
#         new_book.name = request.POST["name"]
#         new_book.author = request.POST["author"]
#         new_book.pages = request.POST['pages']
#         new_book.price = request.POST['price']
#         new_book.desc = request.POST['desc']
#         new_book.image = request.FILES['image']
#         print(new_book)
#         new_book.save()
#         url = reverse('books.data')
#         return redirect(url)
#     return render(request, 'books/book_form.html')

# def create_new_book(request):
#     form = BookForm()
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         # print(request.POST)
#         # print(request.FILES)
#         if form.is_valid():
#             new_book = Book.create_object(request.POST["name"],
#                                             request.POST['desc'],
#                                             request.FILES['image'],
#                                             request.POST["author"],
#                                             request.POST['pages'],
#                                             request.POST['price']
#                                         )
#             url = reverse('books.data')
#             return redirect(url)
    
#     return render(request, 'books/book_form2.html', context={"form": form})


# ===================================== Using DB ================================
def landing(request):
    return render(request, "books/index.html")

def get_books_from_DB(request):
    get_all_books = Book.objects.all()
    return render(request, 'books/all_books_DB.html', context={"books_DB":get_all_books})

def get_book_info_from_DB(request, id):
    book_query = Book.objects.get(id=id)
    return render(request, 'books/bookProfile_DB.html', context={"bookInfo_DB":book_query})

@login_required(login_url='accounts/login')
def create_new_book(request):
    form = BookModelForm()
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save()
            url = reverse('books.data')
            return redirect(url)
    return render(request, 'books/book_form2.html', context={"form": form})


@login_required(login_url='accounts/login')
def edit_book_info_from_DB(request, id):
    selected_book = Book.get_book_by_id(id)
    form = BookModelForm(instance=selected_book)
    if request.method == 'POST':
        form  = BookModelForm(request.POST, request.FILES, instance=selected_book)
        if form.is_valid():
            form.save()
            return redirect(selected_book.show_url)
    return render(request, 'books/book_form_edit.html', context={"form": form})

@login_required(login_url='accounts/login')
def delete_book_from_DB(request, id):
    deleted_book = Book.objects.get(id=id)
    deleted_book.delete()
    url = reverse('books.data')
    return redirect(url)