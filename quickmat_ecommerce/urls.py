# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('store.urls')),
# ]

from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from store import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('store.urls')),
    path('', views.product_list, name='home'), 
    # path('media/<path:path>', views.serve_media, name='media'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
