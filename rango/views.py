from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# import the category model
from rango.models import Category
from rango.models import Page

def index(request):
    # return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict ={}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    pages = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = pages

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # creat a context dictionary(pass the template rendering engine)
    context_dict = {}

    try:
        # .get()method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)

        # retrieve all of the associated pages
        # filter() will return a list of page object or an empty list
        pages = Page.objects.filter(category=category)

        # add results list to the template context under name pages
        context_dict['pages'] = pages
        # use this templates to verify the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    # render the response and return it to client
    return render(request, 'rango/category.html', context=context_dict)