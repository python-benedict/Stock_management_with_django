from django.shortcuts import render
from .models import Articles
import random
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.


#HOME VIEW
def home_view(request):
    articles_obj = Articles.objects.all()
    context = {
        'articles_obj':articles_obj,
    }
    return render(request, 'home.html', context)



# PAGE DETAILED VIEW

def detailed_page(request, id):
    article_obj = Articles.objects.get(id=id)
    context = {
        'article_obj':article_obj
    }
    return render(request, 'detailed_page.html', context=context)

# SEARCH PAGE VIEW

def search_view(request):
    query_dict = request.GET   # This is a dictionary
    #query = query_dict.get('q')     #<input type="text" name="q"/>
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context = {
        'object': article_obj
    }
    return render(request, 'search_view.html', context=context)