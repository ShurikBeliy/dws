from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexDetail.as_view(), name='index_detail_url'),
    path('404/', Page404Detail.as_view(), name='page_404_url'),
]
