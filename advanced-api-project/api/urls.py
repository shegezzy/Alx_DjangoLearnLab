from django.urls import path
from .views import CustomBookListView, CustomBookCreateView, CustomBookDeleteView, CustomBookDetailView, CustomBookUpdateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', CustomBookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail'),
    path('books/create/', CustomBookCreateView.as_view(), name='book-create'),
    path('books/update/', CustomBookUpdateView.as_view(), name='book-update'),
    path('books/delete/', CustomBookDeleteView.as_view(), name='book-delete'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]