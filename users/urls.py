from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="registration_view"),
    path("login/", views.NewLoginView.as_view(), name="login_view"),
    path("users/", views.UserListView.as_view(), name="user_list_view"),
]
