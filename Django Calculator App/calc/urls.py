from django.urls import path
from calc import views

urlpatterns = [
    path('', views.index, name='index'),  # Sử dụng path thay cho url
]
