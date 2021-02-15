from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexDetail.as_view(), name='index_detail_url'),
]
