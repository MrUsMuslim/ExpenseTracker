# Types
from django.http import HttpResponse

# Importing django files
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Import Custom files
from .forms import (
    UserRegisterForm,
    ProfileUpdateForm,
    UserUpdateForm
)

# Others
from expenses.models import Income, Outcome


def home(request: HttpResponse) -> HttpResponse:
    user = User.objects.filter(username = request.user).first()
    income = Income.objects.filter(owner = user)
    outcome = Outcome.objects.filter(owner = user)
    
    context = {
        'database_income': income,
        'database_outcome': outcome
    }
    return render(request, 'Users/home.html', context)

def register(request: HttpResponse) -> HttpResponse:
    """
    Registration page
    """

    if request.method == 'POST':
        form: UserRegisterForm = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You are now able to log in.")
            return redirect('login')
    else:
        form: UserRegisterForm = UserRegisterForm()

    return render(request, 'Users/register.html', {'form': form})


def logout_view(request: HttpResponse) -> HttpResponse:
    """
    Log Out page
    """

    logout(request)
    messages.success(request, "You have been logged out.")
    return render(request, 'Users/logout.html')


@login_required
def profile(request: HttpResponse) -> HttpResponse:
    """
    Profile page
    """

    if request.method == 'POST':
        u_form: UserUpdateForm = UserUpdateForm(request.POST, instance = request.user)
        p_form: ProfileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        # Checking if data is valid
        if u_form.is_valid() and p_form.is_valid():
            # Saving data
            u_form.save()
            p_form.save()

            # Leting user know
            messages.success(request, "Your account has been updated")
            return redirect('profile')
    
    else:
        u_form: UserUpdateForm = UserUpdateForm(instance = request.user)
        p_form: ProfileUpdateForm = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'Users/profile.html', context)