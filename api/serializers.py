from api.models import Books

from rest_framework import serializers

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'isBn', 'isBn13', 'languageCode', 'numPages', 'publicationDate')