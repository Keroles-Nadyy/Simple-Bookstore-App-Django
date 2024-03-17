from django.urls import path
# from books.views import index, get_book, all_books
from books.views import landing, get_books_from_DB, get_book_info_from_DB, create_new_book,delete_book_from_DB, edit_book_info_from_DB


urlpatterns = [
    path('',landing, name="books.landing"),
    path('<int:id>', get_book_info_from_DB, name="book.profile"),
    path('all_books', get_books_from_DB, name='books.data'),
    path('new_book', create_new_book, name='book.creation'),
    path('delete/<int:id>', delete_book_from_DB, name="book.delete"),
    path('edit/<int:id>', edit_book_info_from_DB, name="book.edit")
]