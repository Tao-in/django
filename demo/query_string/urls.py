from django.conf.urls import url
from .import views
urlpatterns = [

    url(r'^index',views.query_str),
    url(r'^weather/([0-9a-zA-Z])/(\d{4})\$',views.weather),



]
