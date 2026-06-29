from django.urls import path
from player.views import home,about,info
urlpatterns = [
    path('',home,name='home'),
    path("about/",about,name='about'),
    path("info/<int:id>/",info,name='info')
]