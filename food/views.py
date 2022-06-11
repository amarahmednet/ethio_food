from .models import item
from django.shortcuts import render

# Create your views here.

def index(request):
    items_ = item.objects.all()
    context = {
    'items_':items_,
    }
    return render(request, 'food/index.html', context)

def detail(request, item_id):
    items = item.objects.get(pk = item_id)
    context = {
        'items':items
    }
    return render(request, 'food/detail.html', context)
