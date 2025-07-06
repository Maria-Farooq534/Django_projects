#I have created this views.py file in textutils project - Maria

#Views responds HTTP request. So, we need to import HTTP
from django.http import HttpResponse

def index(request):  #By default, the index function takes an argument named "request"
    # return "Hello, World" 
    #Now I need to return string in HttpResponse instead of blank string.
    return HttpResponse("Hello, and Welcome")

def about(request):
    # return HttpResponse("About my Website")
    #We can use html tags in it
    return HttpResponse("<h1>About my Website</h1>")
