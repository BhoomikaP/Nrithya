from .views import view1
from django.urls import path

urlpatterns = [
    path('work/', view1)
]
