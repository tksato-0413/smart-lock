from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # リダイレクト先を指定
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})
