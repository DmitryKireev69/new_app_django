from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shipping_and_payment/', views.shipping_and_payment, name='shipping_and_payment'),
    path('contact/', views.contact, name='contact')
]