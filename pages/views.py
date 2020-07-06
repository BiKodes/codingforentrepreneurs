from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    # print(args,kwargs)
    # print(request)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request,*args, **kwargs):
    my_context = {
        "title": "abc this is about code",
        "This is true": True,
        "my_number": 45788555,
        "my_list": [1254,9655,5565,886,"Abc"],
        "my_html": "<h1>Hello World<h1>"
    }
    # return HttpResponse("<h1>Contact page</h1>")
    return render(request, "contact.html", my_context)
