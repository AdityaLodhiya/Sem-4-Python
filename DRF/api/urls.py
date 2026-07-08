from django.urls import path
from api.views import Home,Home2
urlpatterns = [
    path("",Home,name="home"),
    path('home2/',Home2,name='home2')
]
