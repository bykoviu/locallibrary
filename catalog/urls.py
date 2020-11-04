from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
 	path('books/', views.BookListView.as_view(), name='books'),
 	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
         path('genres/', views.GenreListView.as_view(), name='genres')
 	#path('catalog/books/', ),
 	#path('catalog/authors/', ),
 	#path('catalog/book/<id>', ),
 	#path('author/book/<id>', ),
]
