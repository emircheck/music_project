from django.urls import path

from applications.music.views import MusicListView

urlpatterns = [
    path('music-list/', MusicListView.as_view())
]
