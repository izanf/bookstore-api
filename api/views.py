from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.serializers import BooksSerializer
from api.models import Books

# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
  if request.method == 'GET':
    book = Books.objects.all()
    serializer = BooksSerializer(book, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = BooksSerializer(data=request.data)

    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)