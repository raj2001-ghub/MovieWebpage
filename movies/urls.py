from django.urls import path
from . import views
urlpatterns=[
path('',views.home,name="home"),
path('movies/',views.movies,name="movies"),
path('movies/<str:m_name>/',views.movie_description,name="movie_description"),
path('genres/<str:g_name>/',views.genre_list,name="genre_list")
]