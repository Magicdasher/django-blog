from django.contrib import admin
from django.urls import path, include  # Dodaj include, aby włączyć inne aplikacje

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel administracyjny
    path('', include('users.urls')),  # Pozostałe ścieżki aplikacji
]