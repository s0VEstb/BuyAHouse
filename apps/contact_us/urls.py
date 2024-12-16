from django.urls import path
from .views import BannerListCreateAPIView, ContactsListCreateAPIView, FormUsListCreateAPIView

urlpatterns = [
    path('banners/', BannerListCreateAPIView.as_view(), name='banner-list-create'),
    path('contacts/', ContactsListCreateAPIView.as_view(), name='contacts-list-create'),
    path('form-us/', FormUsListCreateAPIView.as_view(), name='form-us-list-create'),
]
