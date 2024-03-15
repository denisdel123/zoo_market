from django.shortcuts import render
from django.urls import reverse_lazy

from transliterate import translit
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from zooApp.models import Category, Dog, Blog


class CategoryListView(ListView):
    """Наследовался от модели Category"""
    model = Category
    """Указал максимальное кол-во карточек на странице (в CBV передает page_obj в контексте под капотом)"""
    paginate_by = 10
    """Функция для передачи доп информации (контекста) в шаблон"""

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        """Добавили поле title и вернули с помощью return"""
        context['title'] = 'Породы'
        return context


"""Класс для создания породы"""


class CategoryCreateView(CreateView):
    model = Category
    """Поля для которые нужно заполнить при создании"""
    fields = ('name', 'description', 'photo')
    """Ссылка по умолчанию по которой пользователь будет переходить после создания породы"""
    success_url = reverse_lazy('zooApp:category')


"""Класс для редактирования породы"""


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'description', 'photo')
    success_url = reverse_lazy('zooApp:category')


"""Класс удаление породы"""


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('zooApp:category')


"""Метод ссылающийся на шаблон настройки"""


def settings(request):
    context = {
        'title': 'Настройки'
    }
    return render(request, 'zooApp/settings.html')


"""Список собак"""


class DogsListView(ListView):
    model = Dog
    paginate_by = 10

    """Передача контекста"""

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Собаки'
        return context

    def get_queryset(self):
        """Извлекаем значение первичного ключа"""
        category_pk = self.kwargs['pk']
        """Выполняем запрос к модели Dog и фильтруем по pk"""
        return Dog.objects.filter(category__pk=category_pk)


"""Класс выводит конкретную собаку"""


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'age', 'description', 'photo', 'price', 'category')

    success_url = reverse_lazy('zooApp:dog_detail')

    """Метод передает pk для того что бы мы могли попасть в карточку только что созданной собаки"""

    def get_success_url(self):
        """Получаем pk"""
        object_id = self.object.pk
        """Передаем pk переходя по url"""
        detail_url = reverse_lazy('zooApp:dog_detail', kwargs={'pk': object_id})
        return detail_url


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'age', 'description', 'photo', 'price', 'category')
    success_url = reverse_lazy('zooApp:dog_detail')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:dog_detail', kwargs={'pk': object_id})
        return detail_url


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('zooApp:category')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:detail_blog')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:detail_blog', kwargs={'pk': object_id})
        return detail_url


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:detail_blog')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:detail_blog', kwargs={'pk': object_id})
        return detail_url


class BlogListView(ListView):
    model = Blog
    template_name = 'zooApp/main_list_true.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'

        return context


"""Класс для не опубликованных блогов"""


class BlogUnpublishedListView(ListView):
    model = Blog
    paginate_by = 10
    template_name = 'zooApp/blog_unpublished.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Не опубликовано'
        return context


class BlogDetailView(DetailView):
    model = Blog

    """Метод для отслеживания просмотров"""

    def get(self, request, *args, **kwargs):
        blog = self.get_object()

        # Увеличиваем счетчик просмотров
        blog.view_count += 1
        blog.save()

        return super().get(request, *args, **kwargs)

    """Создание человекочитаймого slug переводит с русского языка на английский"""

    def create_slug(self, title):
        return translit(title, 'ru', reversed=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        for blog in queryset:
            blog.slug = self.create_slug(blog.title)
            blog.save()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Публикация'
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('zooApp:main')
