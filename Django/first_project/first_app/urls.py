from django.conf.urls import url
from first_app import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('users/', views.users, name='users'),
]
