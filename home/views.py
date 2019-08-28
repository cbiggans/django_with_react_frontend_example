from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

# Create your views here.
# def home(request):
#     return HttpResponse("This is the index")
