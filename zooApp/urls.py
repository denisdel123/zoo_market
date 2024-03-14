from django.urls import path

from zooApp.apps import ZooappConfig
from zooApp.views import CategoryListView, DogsListView, DogDetailView, DogUpdateView, DogCreateView, \
    DogDeleteView, CategoryCreateView, CategoryUpdateView, settings, CategoryDeleteView, BlogCreateView, BlogListView, \
    BlogUpdateView, BlogDetailView, BlogDeleteView, BlogUnpublishedListView

app_name = ZooappConfig.name

urlpatterns = [

    path('settings/', settings, name='settings'),

    path('category/', CategoryListView.as_view(), name='category'),
    path('category/create/', CategoryCreateView.as_view(), name='createcategory'),
    path('<int:pk>category/update/', CategoryUpdateView.as_view(), name='updatecategory'),
    path('<int:pk>category/delete/', CategoryDeleteView.as_view(), name='deletecategory'),

    path('create/dog/', DogCreateView.as_view(), name='createdog'),
    path('<int:pk>dogs/', DogsListView.as_view(), name='dogs'),
    path('<int:pk>dog/detail/', DogDetailView.as_view(), name='dogdetail'),
    path('<int:pk>dog/update/', DogUpdateView.as_view(), name='updatedog'),
    path('<int:pk>dog/delete/', DogDeleteView.as_view(), name='deletedog'),

    path('', BlogListView.as_view(), name='main'),
    path('unpublished', BlogUnpublishedListView.as_view(), name='unpublished'),
    path('blog/create/', BlogCreateView.as_view(), name='createblog'),
    path('<int:pk>blog/update/', BlogUpdateView.as_view(), name='updateblog'),
    path('<int:pk>blog/detail/', BlogDetailView.as_view(), name='detailblog'),
    path('<int:pk>blog/delete/', BlogDeleteView.as_view(), name='deleteblog'),

]
