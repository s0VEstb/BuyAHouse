from rest_framework import generics
from .models import Banner, Contacts, FormUs
from .serializers import BannerSerializer, ContactsSerializer, FormUsSerializer


class BannerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class ContactsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class FormUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = FormUs.objects.all()
    serializer_class = FormUsSerializer
