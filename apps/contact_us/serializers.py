from rest_framework import serializers
from .models import Banner, Contacts, FormUs


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'location', 'open_hours', 'email', 'number']


class FormUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormUs
        fields = ['id', 'name', 'email', 'subject', 'message']
