from django.urls import path
from authors.views import authors_main, show_author, create_author_MF, delete_author_from_DB, edit_author_info_from_DB

urlpatterns = [
    path('',authors_main, name="authors.landing"),
    path('add_author', create_author_MF, name='author.creation'),
    path('<int:id>', show_author, name="author.profile"),
    path('delete/<int:id>', delete_author_from_DB, name="author.delete"),
    path('edit/<int:id>', edit_author_info_from_DB, name="author.edit")
]
