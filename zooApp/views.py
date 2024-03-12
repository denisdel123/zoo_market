from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from zooApp.models import User, Category


class CategoryListView(ListView):
    model = Category


class MainListView(ListView):
    model = Category
    template_name = 'zooApp/main_list.html'
