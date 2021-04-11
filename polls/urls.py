from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:serie>/<str:temporada>/', views.capitulos, name='capitulos'),
    path('<str:serie>/<str:temporada>/<str:capitulo>/', views.episodio, name='episodio'),
    path('search/', views.search, name='search'),
    path('<str:nombre>/', views.personaje, name='personaje')
]
