from django.urls import path

from account.views import user_login, user_logout

app_name = "account"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]