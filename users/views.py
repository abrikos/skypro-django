from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import CustomUserCreationForm, CustomAuthenticationForm, CabinetForm
from users.models import User


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.pug'
    form_class = CustomAuthenticationForm

class RegisterView(CreateView):
    template_name = 'register.pug'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

class CabinetView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = CabinetForm(request.user)
        return render(request, 'cabinet.pug', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CabinetForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('cabinet')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'cabinet.pug', {'form': form})

