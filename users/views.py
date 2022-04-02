from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, VerifyForm, ResendCodeForm
from . import verify
from django.contrib.auth import authenticate, login
from users.decorators import verification_required
from django.contrib import messages

# Create your views here.

@login_required
@verification_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            verify.send(form.cleaned_data.get('phone'))
            return redirect('users:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('users:index')
    else:

        form = VerifyForm()
    return render(request, 'verify.html', {'form': form})

@login_required
def resend_code(request):
    if request.method == 'POST':
        form = ResendCodeForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            if request.user.phone == phone:
                verify.send(phone)
            return redirect('users:verify')
    else:
        form = ResendCodeForm()
    return render(request, 'resend.html', {'form':form})
    

