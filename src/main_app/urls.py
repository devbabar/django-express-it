from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
	
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^user/(\w+)/$',views.profile, name='profile'),
	url(r'^([0-9]+)/$',views.detail, name='detail'),
    url(r'^$',views.index, name='index'),
    url(r'^post/$',views.post_expressit, name='post_expressit'),
    url(r'^accounts/login/$',views.login_view, name='login'),
    url(r'^logout/$',views.logout_view, name='logout'),



]

if settings.DEBUG:
	urlpatterns +=[
	url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
	]

