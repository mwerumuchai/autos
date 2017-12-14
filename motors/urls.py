from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^vehicle/(\d+)$', views.vehicle,name='vehicles'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^vehicle/single-vehicle/(\d+)$', views.single_vehicle,name='single'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
