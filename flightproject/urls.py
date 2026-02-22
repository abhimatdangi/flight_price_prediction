from django.urls import path
from predictor.views import predict
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', predict),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
