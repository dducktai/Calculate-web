from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^$', include('calc.urls')),  # Sử dụng re_path thay cho url
    path('admin/', admin.site.urls),
]
