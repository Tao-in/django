from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^index1',views.Dname.as_view()),




]