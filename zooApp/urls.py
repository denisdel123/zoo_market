from django.urls import path

from zooApp.apps import ZooappConfig
from zooApp.views import CategoryListView, main, DogsListView, DogDetailView, DogUpdateView, DogCreateView, \
    DogDeleteView

app_name = ZooappConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('createdog/', DogCreateView.as_view(), name='createdog'),
    path('dogs/<int:pk>/', DogsListView.as_view(), name='dogs'),
    path('<int:pk>dogdetail/', DogDetailView.as_view(), name='dogdetail'),
    path('<int:pk>updatedog/', DogUpdateView.as_view(), name='updatedog'),
    path('<int:pk>deletedog/', DogDeleteView.as_view(), name='deletedog'),

]
