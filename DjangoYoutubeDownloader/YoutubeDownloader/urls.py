from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('download/', views.download.as_view(), name = "download"),
    path('viewVideo/<str:file>', views.viewVideo, name= "viewVideo" )
]
