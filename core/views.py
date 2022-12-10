from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = "index.html"
    return render(request, template_name)


def about(request):
    template_name = "about.html"
    return render(request, template_name)


def contact(request):
    template_name = "contact.html"
    return render(request, template_name)
