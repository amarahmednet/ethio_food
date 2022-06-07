from django.http import HttpResponse
# from matplotlib.style import context
from .models import item
from django.template import loader
from django.shortcuts import render

# Create your views here.


def index(request):
    index_template = loader.get_template('food/index.html')
    context = {
    #context
    }

    return HttpResponse(index_template.render(context, request))

        