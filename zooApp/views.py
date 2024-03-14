from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from zooApp.models import User, Category, Dog, Blog


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

    success_url = reverse_lazy('zooApp:category')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'age', 'description', 'photo', 'price', 'category')
    success_url = reverse_lazy('zooApp:category')


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('zooApp:category')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:main')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'published',)
    success_url = reverse_lazy('zooApp:main')


class BlogListView(ListView):
    model = Blog
    template_name = 'zooApp/main_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Публикация'
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('zooApp:main')