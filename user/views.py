from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.sucess(request, f'Account created for {username}!')
            return redirect('authentication')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
