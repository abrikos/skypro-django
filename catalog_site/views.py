from django.http import HttpResponse
from django.shortcuts import render

from catalog_site.models import Product, Contacts


# Create your views here.
def product(request, id):
    """View product page"""
    product = Product.objects.get(id=id)
    print(product.image)
    return render(request, 'product.pug', {'product':product})

def home(request):
    """Home page"""
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    """About page"""
    return render(request, 'about.html')

def contacts(request):
    """Contacts page"""
    contacts = Contacts.objects.get()
    return render(request, 'contacts.html', {'contacts':contacts})

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
