from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class HomeView(TemplateView):
    template_name = "home.html"

class ProductListView(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "products"  


class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    fields = ["name", "price", "description"]  
    success_url = reverse_lazy("product_list")  

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product_update.html"
    fields = ["name", "price", "description"]  
    success_url = reverse_lazy("product_list") 

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("product_list")  
