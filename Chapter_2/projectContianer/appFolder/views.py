from django.http import HttpResponse

def HomePageView(self):
    return HttpResponse('This is your home page.')

def AboutPageView(self):
    return HttpResponse('This is your about page.')

# Create your views here.
