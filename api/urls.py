from django.urls import path
from .views import health_check, login_view

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('login/', login_view, name='login'),
]