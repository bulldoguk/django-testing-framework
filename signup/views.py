from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("<h1>Hello, world. You're at the signup index.</h1>")
    return render (request, "signup/main.html")
