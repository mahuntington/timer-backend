from django.urls import path
from . import views

urlpatterns = [
    path('api/sessions', views.SessionList.as_view(), name='session__list'),
    path('api/sessions/<int:pk>', views.SessionDetail.as_view(), name='session_detail'),
]
