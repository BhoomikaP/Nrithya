from .views import feedback_view
from django.urls import path

urlpatterns = [
    path('feedback', feedback_view)
]
