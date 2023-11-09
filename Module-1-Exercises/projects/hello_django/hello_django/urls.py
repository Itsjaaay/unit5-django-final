from django.contrib import admin
from django.urls import path
from app.views import hello


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
]