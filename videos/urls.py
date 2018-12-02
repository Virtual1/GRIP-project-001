from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='inthemix'),
    path('<int:video_id>', views.video, name='video'),
    path('search', views.search, name='search'),
]
