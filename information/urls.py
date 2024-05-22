from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('list/', views.list, name='user_list'),
    path('create/', views.create, name='user_create'),
    path('detail/<int:pk>/', views.detail, name='user_detail'),
    path('update/<int:pk>/', views.update, name='user_update'),
    path('delete/<int:pk>/', views.delete, name='user_confirm_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)