from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from transliterate import translit
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from zooApp.models import Category, Dog, Blog


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Породы'
        return context


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description', 'photo')
    success_url = reverse_lazy('zooApp:category')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'description', 'photo')
    success_url = reverse_lazy('zooApp:category')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('zooApp:category')


def settings(request):
    context = {
        'title': 'Настройки'
    }
    return render(request, 'zooApp/settings.html')


class DogsListView(ListView):
    model = Dog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Собаки'
        return context

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Dog.objects.filter(category__pk=category_pk)


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'age', 'description', 'photo', 'price', 'category')

    success_url = reverse_lazy('zooApp:dogdetail')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:dogdetail', kwargs={'pk': object_id})
        return detail_url


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'age', 'description', 'photo', 'price', 'category')
    success_url = reverse_lazy('zooApp:dogdetail')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:dogdetail', kwargs={'pk': object_id})
        return detail_url


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('zooApp:category')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:detailblog')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:detailblog', kwargs={'pk': object_id})
        return detail_url


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:detailblog')

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('zooApp:detailblog', kwargs={'pk': object_id})
        return detail_url


class BlogListView(ListView):
    model = Blog
    template_name = 'zooApp/main_list_true.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'

        return context


class BlogUnpublishedListView(ListView):
    model = Blog
    template_name = 'zooApp/blog_unpublished.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Не опубликовано'
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        blog = self.get_object()

        # Увеличиваем счетчик просмотров
        blog.view_count += 1
        blog.save()

        return super().get(request, *args, **kwargs)

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
