from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import registerForm
from django.contrib import messages
from passgen.models import password

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome! {username}, your account has been created!')
            return redirect('login')
    else:
        form = registerForm(request.POST)
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    logged_id = request.user.id
    stored_passwords = password.objects.raw(f'SELECT * FROM passgen_password WHERE user_id = {logged_id}')
    
    context={ 'title': 'Profile',
            'stored_passwords': stored_passwords 
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth_logout(request)
    return redirect('home')