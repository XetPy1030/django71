from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]