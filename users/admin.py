from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Dostosowanie panelu administracyjnego dla użytkowników
class CustomUserAdmin(UserAdmin):
    # Pola widoczne w liście użytkowników
    list_display = ('username', 'email', 'is_active', 'last_login', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')  # Filtry po stronie panelu
    search_fields = ('username', 'email')  # Możliwość wyszukiwania po nazwie i e-mailu
    ordering = ('date_joined',)  # Kolejność użytkowników w liście

    # Sekcje w widoku szczegółów użytkownika
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Dane osobowe', {'fields': ('email',)}),
        ('Uprawnienia', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Daty', {'fields': ('last_login', 'date_joined')}),
    )

# Wyrejestrowanie domyślnego modelu User
admin.site.unregister(User)
# Zarejestrowanie zmodyfikowanego panelu dla użytkowników
admin.site.register(User, CustomUserAdmin)
