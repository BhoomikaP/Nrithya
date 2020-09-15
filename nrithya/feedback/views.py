from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Feed
@api_view(['POST'])
def feedback_view(request):
    if request.method == "POST":
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            feeds=request.data.get('feeds')
            context = {
                "name": name,
                "email": email,
                "feeds":feeds,
            }
            r = Feed(**context)
            r.save()
            return Response({"status": "success", "message": "user submitted successfully"})
        except Exception as e:
            return Response({"status": "fail", "message": "user fields are required"}
                    )