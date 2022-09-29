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
