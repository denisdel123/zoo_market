from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from zooApp.models import User, Category, Dog


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description', 'photo')
    success_url = reverse_lazy('zooApp:category')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'description', 'photo')
    success_url = reverse_lazy('zooApp:category')


def main(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'zooApp/main_list.html', context)


def settings(request):
    context = {
        'title': 'Настройки'
    }
    return render(request, 'zooApp/settings.html')


class DogsListView(ListView):
    model = Dog

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
