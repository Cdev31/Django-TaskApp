from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.register ),
    path('login/', views.user_login ),
    path('logout/', views.signup)
]