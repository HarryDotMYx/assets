from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import LoginForm

@ensure_csrf_cookie
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    form = LoginForm()
    error = None
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            error = 'Invalid email or password'
    
    return render(request, 'authentication/login.html', {
        'form': form,
        'error': error
    })

@login_required
@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return redirect('login')