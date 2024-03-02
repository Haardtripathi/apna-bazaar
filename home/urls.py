from django.urls import path
from home.views import *
urlpatterns = [
    path('',index,name='index'),
    path('<slug:category_slug>', products, name='products'),
    path('<int:pk>', product_details, name='product_details')


]
