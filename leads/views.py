from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based views
def home_page(request):
    context={
        "name": "John",
        "age": 35
    }
    # return render(request, "leads/home_page.html")
    return render(request, "second_page.html", context)