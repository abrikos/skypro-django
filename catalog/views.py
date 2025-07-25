from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product, Contacts
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from . import forms

# Create your views here.
class ProductListView(ListView):
    """Products list"""
    model = Product
    template_name = 'list.pug'

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
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'home.html')

class AboutView(TemplateView):
    """About view"""
    template_name='about.html'

class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    """Products delete"""
    model = Product
    template_name = 'product_detail.pug'
    success_url = reverse_lazy('catalog_list')

class CatalogCreateView(LoginRequiredMixin, CreateView):
    """Add Product"""
    model = Product
    form_class = forms.CatalogProductForm
    template_name = 'product_form.pug'
    success_url = reverse_lazy('catalog_list')

class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    """Product update"""
    model = Product
    form_class = forms.CatalogProductForm
    template_name = 'product_form.pug'
    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})


def feedback(request):
    """Accept feedback page"""
    if request.method == 'Product':
        # Получение данных из формы
        print(request.Product)
        name = request.Product.get('name')
        message = request.Product.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'feedback.html')
from django.shortcuts import render

# Create your views here.
