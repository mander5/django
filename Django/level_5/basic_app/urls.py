from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('registration/', views.registration,name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]
