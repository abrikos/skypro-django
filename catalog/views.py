from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView

from catalog.models import Product, Contacts
from . import forms
from django.core.cache import cache

from .services import ProductService


# Create your views here.
class ProductListView(ListView):
    """Products list"""
    model = Product
    template_name = 'list.pug'

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset


class ProductListViewByCategory(TemplateView):
    """Products list by category"""
    model = Product
    template_name = 'list.pug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = ProductService.get_list(self.kwargs.get('pk'))
        context['category_id'] = self.kwargs.get('pk')
        return context


class ProductDetailView(DetailView):
    """Product detail"""
    model = Product
    template_name = 'product_detail.pug'
    def get_context_data(self, **kwargs):
        context = cache.get(f'product-{kwargs['object'].id}')
        if not context:
            context = super().get_context_data(**kwargs)
        return context

class ContactsView(TemplateView):
    """Contacts view"""
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.get()
        return context


class HomeView(TemplateView):
    """Home view"""
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'home.html')


class AboutView(TemplateView):
    """About view"""
    template_name = 'about.html'


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    """Products delete"""
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if product.owner == request.user or request.user.has_perm('catalog.can_delete_product'):
            product.delete()
            return redirect('catalog_list')
        return HttpResponseForbidden("У вас нет прав для удаления продукта.")

class CatalogCreateView(LoginRequiredMixin, CreateView):
    """Add Product"""
    model = Product
    form_class = forms.CatalogProductForm
    template_name = 'product_form.pug'
    success_url = reverse_lazy('catalog_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == self.request.user or request.user.groups.filter(name='Product moderator').exists():
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("You are not Moderator or Owner.")


class CatalogUpdateView(LoginRequiredMixin, ModeratorRequiredMixin, UpdateView):
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
