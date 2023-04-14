from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationForm



def inner(request):
    return render(request, 'inner-page.html')

def base(request):
    return render(request, 'base.html')



def home(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('users-registration')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('my-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})