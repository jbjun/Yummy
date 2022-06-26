from django.urls import path
from . import views

#appname + name으로 이동 경로 지정 가능
app_name = "member"

urlpatterns = [
    # path('login',views.login_view, name="login"),
    # path('logout',views.logout_view, name="logout"),
    # path('signup',views.signup_view, name="signup")
]