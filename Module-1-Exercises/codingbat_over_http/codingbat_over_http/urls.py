
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('warmup-1/near-hundred/<int:num>/', views.near_hundred, name='near_hundred'),
    
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('codingbat/', include('codingbat_app.urls')),
]
