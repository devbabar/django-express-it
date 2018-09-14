from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from main_app import views
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/',include(admin.site.urls)),
    url(r'^',include('main_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



'''Django Debug Toolbar Setting'''

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]