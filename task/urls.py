from django.urls import path
from . import views


urlpatterns = [
    path('', views.task ),
    path('<int:id>/',  views.detail_task),
    path('create/', views.create),
    path('categories/', views.categories ),
    path('categories/create', views.create_category),
    path('categories/delete/<int:id>/', views.delete_category, name='delete_category')
]