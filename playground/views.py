from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

# String Message 
def test_api(request):
    return HttpResponse("First API")

# Json Message
def test_json_api(request):
    data = {
        "name" : "First Json API",
        "framework" : "Python-Django",
        "university" : "Sit"
    }
    return JsonResponse(data)

# HTMl Template
def test_html_page(request):
    data = {
        "name" : "First Json API",
        "framework" : "Python-Django",
        "university" : "Sit"
    }
    return render(request, "playground/index.html", data)


