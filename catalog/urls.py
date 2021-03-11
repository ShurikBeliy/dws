from django.urls import path
from .views import *

urlpatterns = [
        path('', CategoryList.as_view(), name='category_list_url'),
        path('<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
]
