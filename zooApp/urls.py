from django.urls import path

from zooApp.apps import ZooappConfig
from zooApp.views import CategoryListView, MainListView

app_name = ZooappConfig.name

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
    path('', MainListView.as_view(), name='main'),

]
