from django.urls import path

from zooApp.apps import ZooappConfig
from zooApp.views import CategoryListView, DogsListView, DogDetailView, DogUpdateView, DogCreateView, \
    DogDeleteView, CategoryCreateView, CategoryUpdateView, settings, CategoryDeleteView, BlogCreateView, BlogListView, \
    BlogUpdateView, BlogDetailView, BlogDeleteView, BlogUnpublishedListView

app_name = ZooappConfig.name

urlpatterns = [

    path('settings/', settings, name='settings'),

    path('category/', CategoryListView.as_view(), name='category'),
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('<int:pk>category/update/', CategoryUpdateView.as_view(), name='update_category'),
    path('<int:pk>category/delete/', CategoryDeleteView.as_view(), name='delete_category'),

    path('create/dog/', DogCreateView.as_view(), name='create_dog'),
    path('<int:pk>dogs/', DogsListView.as_view(), name='dogs'),
    path('<int:pk>dog/detail/', DogDetailView.as_view(), name='dog_detail'),
    path('<int:pk>dog/update/', DogUpdateView.as_view(), name='update_dog'),
    path('<int:pk>dog/delete/', DogDeleteView.as_view(), name='delete_dog'),

    path('', BlogListView.as_view(), name='main'),
    path('unpublished', BlogUnpublishedListView.as_view(), name='unpublished'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>blog/update/', BlogUpdateView.as_view(), name='update_blog'),
    path('<int:pk>blog/detail/', BlogDetailView.as_view(), name='detail_blog'),
    path('<int:pk>blog/delete/', BlogDeleteView.as_view(), name='delete_blog'),

]
