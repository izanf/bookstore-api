from api.models import Books

from rest_framework import serializers

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'authors', 'categories', 'image', 'info_link', 'language', 'maturity_rating', 'page_count', 'published_date', 'publisher', 'title', 'subtitle', 'description')