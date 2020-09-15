from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from Register.serializers import UserSerializer
from Register.models import User
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        try:
            email = request.data.get("email")
            first_name = request.data.get("first_name")
            username = request.data.get("username")
            phone = request.data.get("phone")
            password = request.data.get("password")
            # hello = request.data.get("hello")
            context = {
                "email": email,
                "first_name": first_name,
                "username": username,
                "phone": phone,
                "password": password,
            }
            r = User(**context)
            r.save()
            return Response({"status": "success",  "status": "success", "code": "200"})

        except Exception as e:
            return Response({"status": "fail", "message": "user fields are required"})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        try:
            user = request.data.get('Username')
            psw = request.data.get('Password')
            users = User.objects.get(username=user)
            if users.password == psw:
                return Response({"message": "Login successful", "status": "success", "code": "200"})
            else:
                return Response({"message": "invalid credentials", "status": "failed"})
        except Exception as e:
            return Response(str(e))

