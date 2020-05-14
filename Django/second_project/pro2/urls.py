from django.conf.urls import url
from pro2 import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('help/',views.help, name='help'),
]
