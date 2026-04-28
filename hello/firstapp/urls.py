from django.urls import path
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^contact/', views.contact, name='contact'),
    re_path(r'^about', views.about, name='about'),
    # re_path(r'^product/(?P<productid>\d+)/', views.product),
    path('product/<int:productid>/', views.product),
    path('product/', views.product),
    # re_path(r'^user/(?P<id>\d+)/(?P<name>\D+)/', views.user),
    path('user/', views.user),
    path('user/<int:id>/<name>/', views.user),
    path('details/', views.details),
    path('', views.index, name='index'),
    path('access/<int:age>', views.access)
]