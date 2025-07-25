from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from my_site import settings
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
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

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

