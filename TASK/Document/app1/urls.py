from django.urls import path
from . import views

urlpatterns=[
    path('upload/',views.upload,name='upload'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('view/<int:pk>/',views.view,name='view'),
    path('download/<int:pk>/',views.download,name='download')
]