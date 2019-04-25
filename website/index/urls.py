from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('en/documentation-en', views.documentation, name='documentation'),
]
