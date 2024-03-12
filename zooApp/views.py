from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from zooApp.models import User, Category, Dog


class CategoryListView(ListView):
    model = Category


def main(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'zooApp/main_list.html', context)


class DogsListView(ListView):
    model = Dog


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
