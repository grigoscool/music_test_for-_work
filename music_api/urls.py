from django.urls import path

from . import views

urlpatterns = [
    path('musician-list/', views.MusicianListApiView.as_view()),
    path('album-list/', views.AlbumListApiView.as_view()),
    path('track-list/', views.TrackListApiView.as_view()),
    path('musician-retrieve/<int:pk>/',
         views.MusicianRetrieveApiView.as_view()),
    path('album-creation/', views.AlbumCreationApiView.as_view()),
    path('track-delete/<int:pk>/', views.TrackDeleteApiView.as_view()),
]
