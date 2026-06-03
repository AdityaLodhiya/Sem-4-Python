from django.urls import path
from app2.views import contact,base
urlpatterns=[
    path('contact/',contact,name='contact'),
    path('base/',base,name='base')
]