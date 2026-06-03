from django.urls import path
from app1.views import home,det
urlpatterns=[
    path('',home,name='home'),
    path('det/<int:student_id>',det,name='inf')
]