from django.conf.urls import url
from web import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.get_reminder, name='reminder'),
    url(r'^uber/$', views.get_uber_time, name='uber'),
    url(r'^maps/$', views.get_maps_time, name='maps'),
    url(r'^email/$', views.send_email, name='email'),
]
