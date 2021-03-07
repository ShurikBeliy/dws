from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import IndexDetail, Page404Detail

urlpatterns = [
    path('dws-admin/', admin.site.urls),
    path('', IndexDetail.as_view(), name='index_detail_url'),
    path('404/', Page404Detail.as_view(), name='page_404_url'),
    path('catalog/',include('catalog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
