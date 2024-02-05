from django.urls import path
from . import views


urlpatterns = [
    path('', views.task ),
    path('<int:id>/',  views.detail_task),
    path('create/', views.create)
]