from django.urls import path
from student.views import home,info,form,edit,delete_obj
urlpatterns = [
    path("",home,name='home'),
    path("info/<int:id>",info,name='info'),
    path("form/",form,name='form'),
    path("edit/<int:id>",edit,name='edit'),
    path("delete_obj/<int:id>",delete_obj,name='delete_obj')
]
