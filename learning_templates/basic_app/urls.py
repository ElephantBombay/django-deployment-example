from django.conf.urls import url
from basic_app import views

urlpatterns = [
    url('',views.index,name = 'index'),
]
