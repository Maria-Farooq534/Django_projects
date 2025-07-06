#I have created this views.py file in textutils project - Maria

#Views responds HTTP request. So, we need to import HTTP
from django.http import HttpResponse

def index(request):  #By default, the index function takes an argument named "request"
    # return "Hello, World" 
    #Now I need to return string in HttpResponse instead of blank string.
    return HttpResponse("""Hello, and Welcome!
                        <h5>Here you can Check:</h5>
                        <h6>about</h6>
                        <h6>profiles</h6>
                        <h6>services</h6>
                        
                        """)

def about(request):
    # return HttpResponse("About my Website")
    #We can use html tags in it
    return HttpResponse("<h1>About me</h1>")

def profiles(request):
    return HttpResponse("""
                        Visit my Profiles:
                        <a href="https://github.com/Maria-Farooq534">GitHub</a>
                        <a href = "http://www.linkedin.com/in/maria-farooq-b693b7288">LinkedIn</a>
                        <a href = "https://www.behance.net/mariafarooq5">Behance</a>
                        """)

def services(request):
    return HttpResponse("No Service for now :)")
