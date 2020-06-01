from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('checkout-page/', views.checkout_page, name="checkout_page"),
    path('product-list/', views.products, name="products"),
    url(r'^products/(?P<slug>[\w-]+)/$', views.ItemDetailView.as_view(), name="product")
]