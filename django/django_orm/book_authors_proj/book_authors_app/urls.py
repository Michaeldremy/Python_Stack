from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.index_authors),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('books/<int:booksID>', views.index_books),
    path('authors/<int:authorsID>', views.index_author_info)
]