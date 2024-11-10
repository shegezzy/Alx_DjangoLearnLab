# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView
from .views import register

urlpatterns = [
    path('login/<int:pk>/', LoginView.as_view(template_name='login'), name='login'),
    path('logout/<int:pk>/', LogoutView.as_view(template_name='logout'), name='logout'),
    path('register/', register, name='views.register'),
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  
]