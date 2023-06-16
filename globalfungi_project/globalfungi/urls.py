
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),  # Define your home view and URL pattern
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]
