from django.urls import path

from zooApp.apps import ZooappConfig
from zooApp.views import CategoryListView, main, DogsListView, DogDetailView, DogUpdateView, DogCreateView, \
    DogDeleteView, CategoryCreateView, CategoryUpdateView, settings

app_name = ZooappConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('settings/', settings, name='settings'),


    path('category/', CategoryListView.as_view(), name='category'),
    path('createcategory/', CategoryCreateView.as_view(), name='createcategory'),
    path('<int:pk>updatecategory/', CategoryUpdateView.as_view(), name='updatecategory'),

    path('createdog/', DogCreateView.as_view(), name='createdog'),
    path('<int:pk>dogs/', DogsListView.as_view(), name='dogs'),
    path('<int:pk>dogdetail/', DogDetailView.as_view(), name='dogdetail'),
    path('<int:pk>updatedog/', DogUpdateView.as_view(), name='updatedog'),
    path('<int:pk>deletedog/', DogDeleteView.as_view(), name='deletedog'),

]
