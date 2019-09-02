from django.conf.urls import url
from . import views
                    
urlpatterns = [
     url(r'^$', views.index),
     url(r'^process$', views.regi),
     url(r'^process/login$', views.login),
     url(r'^dashboard$', views.dashbord),
     url(r'^jobs/new$', views.add),
     url(r'^jobs/process$', views.add_process),
     url(r'^jobs/edit(?P<idr>\d+)$', views.edit),
     url(r'^edit/(?P<idr>\d+)/process$', views.edit_process),
     url(r'^jobs/(?P<idr>\d+)$', views.show),
     url(r'^destroy$', views.destroy),
     url(r'^jobs/(?P<idr>\d+)/delete$', views.delete),
]