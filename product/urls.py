from django.urls import path
from .views import (
    HomeView, ProductListView, 
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/new/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
