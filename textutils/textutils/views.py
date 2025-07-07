#I have created this views.py file in textutils project - Maria

#Views responds HTTP request. So, we need to import HTTP
from django.http import HttpResponse

# def index(request):  #By default, the index function takes an argument named "request"
#     # return "Hello, World" 
#     #Now I need to return string in HttpResponse instead of blank string.
#     return HttpResponse("""Hello, and Welcome!
#                         <h5>Here you can Check:</h5>
#                         <h6>about</h6>
#                         <h6>profiles</h6>
#                         <h6>services</h6>
                    
                        
#                         """)

# def about(request):
#     # return HttpResponse("About my Website")
#     #We can use html tags in it
#     return HttpResponse("<h1>About me</h1>")

# def profiles(request):
#     return HttpResponse("""
#                         Visit my Profiles:
#                         <a href="https://github.com/Maria-Farooq534">GitHub</a>
#                         <a href = "http://www.linkedin.com/in/maria-farooq-b693b7288">LinkedIn</a>
#                         <a href = "https://www.behance.net/mariafarooq5">Behance</a>
#                         <a href = "https://github.com/fahad-maqbool/SEOOnt">SEO Ontology Project</a>
#                         """)

# def services(request):
#     return HttpResponse("No Service for now :)")



def index(request):
    return HttpResponse("""Home
                        
                        <h5><a href = "">News</a></h5>
                        <h5><a href = "">Services</a></h5>
                        <h5><a href = "">Profiles</a></h5>
                        <h5><a href = "">Contaxt</a></h5>
                        <h5><a href = "">About</a></h5>

                        """)
def news(request):
    return HttpResponse("""This is about News                        
                        <h5><a href = "http://127.0.0.1:8000/">Back To Home</a></h5>
                        """)

def services(request):
    return HttpResponse("""This page is about services                        
                        <h5><a href = "http://127.0.0.1:8000/">Back To Home</a></h5>                        
                        """)
def profiles(request):
    return HttpResponse("""
#                         Visit my Profiles:
#                         <a href="https://github.com/Maria-Farooq534">GitHub</a>
#                         <a href = "http://www.linkedin.com/in/maria-farooq-b693b7288">LinkedIn</a>
#                         <a href = "https://www.behance.net/mariafarooq5">Behance</a>
#                         <a href = "https://github.com/fahad-maqbool/SEOOnt">SEO Ontology Project</a>
                        
                        <h5><a href = "http://127.0.0.1:8000/">Back To Home</a></h5> 
#                         """)

def contact(request):
    return HttpResponse("""Conntact Us                        
                        <h5><a href = "http://127.0.0.1:8000/">Back To Home</a></h5>                        
                        """)
def about(request):
    return HttpResponse("""About Us                        
                        <h5><a href = "http://127.0.0.1:8000/">Back To Home</a></h5>                        
                        """)
