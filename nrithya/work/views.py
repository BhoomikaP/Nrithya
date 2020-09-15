from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work
@api_view(['POST'])
def view1(request):
    if request.method == "POST":
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            gender = request.data.get('gender')
            phone = request.data.get('phone')
            birthday = request.data.get('birthday')
            experience = request.data.get('experience')
            years = request.data.get('years')
            months = request.data.get('months')
            currentsalary = request.data.get('currentsalary')
            expectedsalary = request.data.get('expectedsalary')
            nameofdegree = request.data.get('nameofdegree')
            passyear = request.data.get('passyear')
            formsknown = request.data.get('formsknown')
            context = {
                "name": name,
                "email": email,
                "gender": gender,
                "phone": phone,
                "birthday":birthday,
                "experience":experience,
                "years":years,
                "months":months,
                "currentsalary":currentsalary,
                "expectedsalary":expectedsalary,
                "nameofdegree":nameofdegree,
                "passyear":passyear,
                "formsknown":formsknown,


            }
            r = Work(**context)
            r.save()
            return Response({"status": "success", "message": "user registered successfully for work"})
        except Exception as e:
            return Response({"status": "fail", "message": "user fields are required"}
                            )