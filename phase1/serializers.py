from rest_framework import serializers

from phase1.models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model=News
        fields=("title","date","description","categories")
        depth=1