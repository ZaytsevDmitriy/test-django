from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    path('contact/', TemplateView.as_view(template_name='firstapp/contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='firstapp/about.html',
         extra_context={"work":"Разработка програмных продуктов"})),
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