from .models import item
from django.shortcuts import render

# Create your views here.

def index(request):
    # index_template = loader.get_template('food/index.html')
    items_ = item.objects.all()
    context = {
    #context
    'items_':items_,
    }
    return render(request, 'food/index.html', context)

def detail(request, item_id):

    items = item.objects.get(pk = item_id)

    context = {
        'items':items
    }
    
    return render(request, 'food/detail.html', context)