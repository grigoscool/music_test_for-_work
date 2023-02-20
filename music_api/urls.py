from django.urls import path

from . import views


urlpatterns = [
    path('musician-list/', views.MusicianListApiView.as_view()),
]
