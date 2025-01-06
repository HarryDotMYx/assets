from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'),
    path('', include('authentication.urls')),
    path('', include('assets.urls')),  # Add this line
]