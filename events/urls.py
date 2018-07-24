from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from events import views


urlpatterns = [
    path('events/', views.events, name="events"),
    path('newevent/', views.createEvent, name="newevent"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
