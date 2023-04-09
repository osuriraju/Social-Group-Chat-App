from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('signup', views.signup),
    path('addpost', views.addpost),
    path('addprofilepic', views.addprofilepic),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
