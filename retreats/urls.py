from django.urls import path
from . import views

urlpatterns = [
    path('', views.retreats, name='retreats'),
    path('add/', views.add_retreat, name='add_retreat'),
    path('edit_retreat/<int:retreat_id>/', views.edit_retreat, name='edit_retreat'),
    path('<int:retreat_id>/', views.retreat_detail, name='retreat_detail'),
    path('delete/<int:retreat_id>/', views.delete_retreat, name='delete_retreat'),
]