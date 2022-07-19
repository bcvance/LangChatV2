from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/", views.chat, name="chat"),
    # path("api/users/<int:room_name>", views.get_users, name="users"),
]