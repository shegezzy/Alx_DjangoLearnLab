from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from .models import Book

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
# Create your views here.
