from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

from api.serializers import BooksSerializer
from api.models import Books

class BooksList(APIView):
    def get(self, request, format=None):
        books = Books.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            books = books.filter(title=title)
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookItem(APIView):
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    def patch(self, request, pk):
        book = self.get_object(pk)
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        testmodel_object = self.get_object(pk)
        serializer = TestModelSerializer(testmodel_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
