from django.urls import path
from . import views


urlpatterns = [
    path('hey/<str:name>/', views.hey, name='hey'),
    path('age-in/<int:end>/<int:birthyear>/', views.age_in, name='age_in'),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>/', views.order_total, name='order_total'),
]

