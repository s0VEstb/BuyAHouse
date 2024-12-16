from django.urls import path
from .views import BannerListCreateAPIView, HousesListCreateAPIView, MiniCardsListCreateAPIView, ReviewsListCreateAPIView, OurAgentsListCreateAPIView, FooterListCreateAPIView, AdvantagesListCreateAPIView, NumbersListCreateAPIView

urlpatterns = [
    path('banners/', BannerListCreateAPIView.as_view(), name='banner-list-create'),
    path('houses/', HousesListCreateAPIView.as_view(), name='houses-list-create'),
    path('mini-cards/', MiniCardsListCreateAPIView.as_view(), name='mini-cards-list-create'),
    path('reviews/', ReviewsListCreateAPIView.as_view(), name='reviews-list-create'),
    path('our-agents/', OurAgentsListCreateAPIView.as_view(), name='our-agents-list-create'),
    path('footer/', FooterListCreateAPIView.as_view(), name='footer-list-create'),
    path('advantages/', AdvantagesListCreateAPIView.as_view(), name='advantages-list-create'),
    path('numbers/', NumbersListCreateAPIView.as_view(), name='numbers-list-create'),
]
