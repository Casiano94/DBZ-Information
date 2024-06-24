from django.urls import path
from .views import FighterListView

urlpatterns = [
    path('fighters/', FighterListView.as_view(), name='fighter-list'),
]
