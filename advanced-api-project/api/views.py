from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookDetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = Book.objects.all()
    permission_classes = [IsAuthenticated]

class CustomBookDeleteView(generics.DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class = Book.objects.all()
    permission_classes = [IsAuthenticated]

# only authenticated users can update, delete and add books in this application.
# Create your views here.
