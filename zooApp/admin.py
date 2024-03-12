from django.contrib import admin

from zooApp.models import Category, Dog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', )


