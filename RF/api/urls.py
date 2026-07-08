from django.urls import path
from api.views import Api_demo,Api_detail
urlpatterns = [
    path('api_demo/',Api_demo,name='home'),
    path('api_detail/<int:id>/',Api_detail,name='api_detail')
]
