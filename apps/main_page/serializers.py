from rest_framework import serializers
from .models import Banner, Houses, MiniCards, Reviews, OurAgents, Footer, Advantages, Numbers


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image']


class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ['id', 'image', 'price', 'addres', 'state', 'first_description', 'second_description']


class MiniCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniCards
        fields = ['id', 'image', 'title', 'description']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'image', 'star', 'name', 'description', 'profession']


class OurAgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAgents
        fields = ['id', 'image', 'name', 'profession', 'description', 'link1', 'link2', 'link3', 'link4']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'addres', 'number1', 'number2', 'mail']


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['id', 'image', 'title', 'description']


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ['id', 'number', 'description']
