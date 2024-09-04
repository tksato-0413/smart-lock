from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.http import HttpResponse
import requests
from dotenv import load_dotenv
import os



def home(request):
    return render(request,'home.html')

def control_motor(request):
    if request.method == "POST":
        try:
            # .env ファイルの読み込み
            load_dotenv()

            # 環境変数からIPアドレスを取得
            raspberry_pi_ip = os.getenv('')
            url = f'http://{raspberry_pi_ip}:556/run_motor'  # Replace <raspberry_pi_ip> with your Raspberry Pi's IP
            response = requests.post(url)
            if response.status_code == 200:
                return HttpResponse('Motor activated')
            else:
                return HttpResponse('Failed to activate motor')
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}')
    else:
        return render(request, 'home.html')

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
