from django.shortcuts import render


# Create your views here.


def home_page(request):
    return render(request, '/home/blackthunder/PycharmProjects/SardorBlogs/templates/index.html')
