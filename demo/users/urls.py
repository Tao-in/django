from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^index1', views.index1),

    url(r'^index',views.index ),



]

