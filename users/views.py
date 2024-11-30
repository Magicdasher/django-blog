from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Rejestracja użytkownika
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Niestandardowe wylogowanie
def custom_logout(request):
    logout(request)  # Wylogowanie użytkownika
    return redirect('homepage')  # Przekierowanie na stronę główną

@login_required
def blog_home(request):
    return render(request, 'users/blog_home.html', {'username': request.user.username})

# Strona główna dla niezalogowanych użytkowników
def homepage(request):
    if request.user.is_authenticated:
        return redirect('blog_home')  # Jeśli użytkownik jest zalogowany, przekieruj na blog_home
    return render(request, 'users/homepage.html')  # Dla niezalogowanych wyświetl stronę główną
