from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import LoginForm

def health_check(request):
    return JsonResponse({'status': 'ok'})

@ensure_csrf_cookie
def login_view(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'error'}, status=401)
    
    return render(request, 'api/login.html', {'form': form})