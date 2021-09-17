from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from product.views import CreateProductView, ProductDetailView, UpdateProductView, DeleteProductView, ProductListView
from review.views import ReviewListView, DeleteReviewView, UpdateReviewView, ReviewDetailView, CreateReviewView

urlpatterns = [
    path('create/', CreateReviewView.as_view()),
    path('retrieve/<int:id>/', ReviewDetailView.as_view()),
    path('update/<int:id>/', UpdateReviewView.as_view()),
    path('delete/<int:id>/', DeleteReviewView.as_view()),
    path('list/', ReviewListView.as_view()),
]