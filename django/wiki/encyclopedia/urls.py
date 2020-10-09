from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search", views.search, name="search"),
    path("new-entry", views.new_entry, name="new entry"),
    path("edit-page/<str:title>", views.edit_page, name="edit page"),
    path("random-page", views.random_page, name="random page")
]
