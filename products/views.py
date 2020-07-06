from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product

from .forms import ProductForm, RawProductForm

# Create your views here.

# def dynamic_lookup_view(request, id):
#     # obj = Product.objects.get(id=1)
#     # obj =  get_object_or_404(Product, id=id)
#     try:
#         obj = Product.objects.get(id=id)
#
#     except Product.DoesNotExist:
#         raise Http404
#
#         context = {
#         "object": obj
#         }
#     return render(request,'products/product_detail.html', context)

def product_list_view(request):
    queryset = Product.objects.all()  #List of objects
    context = {
            "object_list": queryset
        }
    return render(request, 'products/product_list.html', context)


# def product_delete_view(request, id):
#     # obj = Product.objects.get(id=1)
#     # obj =  get_object_or_404(Product, id=id)
#
#     obj = get_object_or_404(Product, id=id)
#     #POST request
#     if request.method == "POST":
#         #confirming delete
#         obj.delete()
#         return redirect('../')
#
#         context = {
#             "object": obj
#         }
#     return render(request,'products/product_delete.html', context)



# def render_initial_data(request):
#
#     initial_data = {
#         'title': "My awesome title"
#     }
#
#     obj = Product.objects.get(id=1)
#     form = RawProductForm(request.POST or None, initial=initial_data, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form
#     }
#     return render(request,'products/product_create.html', context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             #now the data is good
#         else:
#             print(my_form.errors)
#
#     context = {
#             "form": my_form
#         }
#     return render(request,'products/product_create.html', context)
#


# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     # product.objects.create(title = my_new_title)
#     context = {}
#     return render(request,'products/product_create.html', context)
#
#
#
#

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#         'form': form
#     }
#
#     return render(request,'products/product_create.html', context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)

    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price ': obj.price,
    # }

    context = {
        "object": obj
    }
    
    return render(request,'products/product_detail.html', context)
