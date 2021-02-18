from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    url(r'^department/$', views.departmentAPI),
    url(r'^department/(0-9+)$', views.departmentAPI),
    url(r'^employee/$', views.employeAPI),
    url(r'^employee/(0-9+)$', views.employeAPI),
    url(r'^SaveFiles$', views.upload_File),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)