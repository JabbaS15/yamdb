import datetime as dt

from django.db.models import Avg
from rest_framework import serializers
from rest_framework.serializers import (SlugRelatedField, CharField,
                                        CurrentUserDefault)

from reviews.models import Category, Comment, Genre, Review, Title


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        rating = Review.objects.filter(
            title=obj.id).aggregate(Avg('score'))
        return rating['score__avg']


class TitleRecordSerializer(serializers.ModelSerializer):
    genre = SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    category = SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    description = CharField(required=False)

    class Meta:
        model = Title
        fields = '__all__'

    def validate_year(self, value):
        year = dt.date.today().year
        if year < value:
            raise serializers.ValidationError(
                'Проверьте год создания произведения!'
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username',
        default=CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'score')
        model = Review

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = (
            self.context['request'].parser_context['kwargs']['title_id']
        )
        author = self.context['request'].user
        if (
            Review.objects.filter(
                author=author, title__id=title_id).exists()
        ):
            raise serializers.ValidationError(
                "Вами уже был оставлен отзыв на это произведение")
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username',
        default=CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
