from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def feedback(request):
    if request.method == 'POST':
        # Получение данных из формы
        print(request.POST)
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'feedback.html')
