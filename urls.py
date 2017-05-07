from django.conf.urls import url
from todos import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name = "create"),
    url(r'^contact$', views.contact, name= "contact"),
    url(r'^about$', views.about, name= "about"),
    url(r'^save$', views.save, name= "save"),
    url(r'^edit/(\d+)/$', views.edit, name= "edit"),
    url(r'^remove/(\d+)/$', views.remove, name= "remove"),
    ]
