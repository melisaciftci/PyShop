from django.urls import path
from . import views


# . means current folder
# views is a generic name, python takes that as another library, we need to use from .

# /products
#/products/1/detail
urlpatterns = [
    path('', views.index), #not calling,
    # passing the reference
    path('new', views.new)

]