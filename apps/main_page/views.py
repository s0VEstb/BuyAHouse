from rest_framework import generics
from .models import Banner, Houses, MiniCards, Reviews, OurAgents, Footer, Advantages, Numbers
from .serializers import BannerSerializer, HousesSerializer, MiniCardsSerializer, ReviewsSerializer, OurAgentsSerializer, FooterSerializer, AdvantagesSerializer, NumbersSerializer


class BannerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class HousesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesSerializer


class MiniCardsListCreateAPIView(generics.ListCreateAPIView):
    queryset = MiniCards.objects.all()
    serializer_class = MiniCardsSerializer


class ReviewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class OurAgentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = OurAgents.objects.all()
    serializer_class = OurAgentsSerializer


class FooterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class AdvantagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer


class NumbersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer
