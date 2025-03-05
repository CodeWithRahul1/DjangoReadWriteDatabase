from django.urls import path
from .views import UserRegisterView, UserLoginView, ProductCreateView, ProductListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('product-register/', ProductCreateView.as_view(), name='product-register'),
    path('list/', ProductListView.as_view(), name='product-list'),
]
