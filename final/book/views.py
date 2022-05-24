from django.shortcuts import get_object_or_404, render
from requests import Response

from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer

# Create your views here.


@api_view(['GET'])
def list(request):

    # permission_classes = (IsAuthenticated,)

    try:
        items = Book.objects.all()

        serialized = BookSerializer(items)

        return Response(serialized)

    except:
        return Response(status=404)


@api_view(['POST'])
def post(request):
    book = BookSerializer(data=request.data)

    if book.is_valid():
        book.save()
        return Response(book.data)
    
    else:
        return Response(status=404)

    

@api_view(['DELTE'])
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    book.delete()

    return Response(status=202)


