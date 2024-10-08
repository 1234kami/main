from rest_framework import serializers
from .models import News, NewsImage

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ('id', 'image', 'title')

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'language', 'title', 'content', 'category', 'views', 'publication_date', 'images')
