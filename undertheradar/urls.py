from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup_page/", SignUpView.as_view(), name="signup"),
]