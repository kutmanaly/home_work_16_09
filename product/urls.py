from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from product.views import CreateProductView, ProductDetailView, UpdateProductView, DeleteProductView, ProductListView

urlpatterns = [
    path('create/', CreateProductView.as_view()),
    path('retrieve/<int:id>/', ProductDetailView.as_view()),
    path('update/<int:id>/', UpdateProductView.as_view()),
    path('delete/<int:id>/', DeleteProductView.as_view()),
    path('list/', ProductListView.as_view()),
]
