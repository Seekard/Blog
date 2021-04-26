from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('zapiski', PublicationList.as_view(), name='PublicationList'),
    path('publication/<slug:slug>', SinglePublication.as_view(), name='SinglePublication'),
    path('publish', AddPublication.as_view(), name='AddPublication')
]
