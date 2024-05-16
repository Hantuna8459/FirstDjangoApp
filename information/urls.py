from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.list, name='user_list'),
    path('user/create/', views.create, name='user_create'),
    path('user/<int:pk>/', views.detail, name='user_detail'),
    path('user/<int:pk>/update/', views.update, name='user_update'),
    path('user/<int:pk>/delete/', views.delete, name='user_confirm_delete'),
]
