from django.urls import path
from .views import *

urlpatterns = [
        path('<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
]
