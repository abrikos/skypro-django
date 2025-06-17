from django.http import HttpResponse
from django.shortcuts import render

from catalog_site.models import Product, Contacts
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
class ProductListView(ListView):
    """Products list"""
    model = Product
    template_name = 'catalog.pug'

class ProductDetailView(DetailView):
    """Product detail"""
    model = Product
    template_name = 'product_detail.pug'

class ContactsView(TemplateView):
    """Contacts view"""
    template_name='contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts']= Contacts.objects.get()
        return context

class HomeView(TemplateView):
    """Home view"""
    template_name='home.html'

class AboutView(TemplateView):
    """About view"""
    template_name='about.html'


def feedback(request):
    """Accept feedback page"""
    if request.method == 'POST':
        # Получение данных из формы
        print(request.POST)
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'feedback.html')
from django.shortcuts import render

# Create your views here.
