from django.urls import path

from Register.views import register_view, login

urlpatterns = [
    path('Register/',register_view),
    path('login/',login),

]