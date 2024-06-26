from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="root_paginate"),
    # path("author/<int:_id>/", views.show_author, name="show_author"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("add_author/", views.add_author, name="add_author"),
    path("add_tag/", views.add_tag, name="add_tag"),
    path("show_author/<int:author_id>", views.show_author, name="show_author"),
    path("viewing_tag/<str:tag_name>", views.viewing_tag, name="viewing_tag"),

]