from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон


# создаём представление, в котором будут детали конкретного отдельного товара
class NewsDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'newsone.html' # название шаблона будет product.html
    context_object_name = 'new' # название объекта
# Create your views here.
