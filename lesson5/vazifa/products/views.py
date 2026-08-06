from django.shortcuts import render
from django.views import View
from .utils import get_categories, get_category_child,get_category_not_child,get_product_ordering

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class IndexView(View):
    def get(self,request):
        
        context = {
            'categories' : get_categories(),
            'get_category_child':get_category_child(),
            'get_category_not_child': get_category_not_child(),
            'get_product_ordering':get_product_ordering()
        }

        return render(request, 'index.html', context)