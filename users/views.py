from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, VerifyForm
from . import verify
# Create your views here.

@login_required
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
