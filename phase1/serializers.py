from rest_framework import serializers

from phase1.models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'date', 'description', 'categories', 'categorized')

    categories = CategorySerializer(many=True, read_only=True)

    def save(self, **kwargs):
        return super().save(team=self.context['request'].team, **kwargs)