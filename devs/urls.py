from django.urls import path
from .views import DevListView

urlpatterns = [
    path('', DevListView.as_view())
]